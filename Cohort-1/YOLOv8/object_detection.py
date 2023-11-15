import torch
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from ultralytics import YOLO

import ray
from ray import serve
from ray.serve.handle import DeploymentHandle

ray.init()
serve.start(http_options={"host": "0.0.0.0", "port": 8000})

app = FastAPI()

@serve.deployment(num_replicas=1)
@serve.ingress(app)
class APIIngress:
    def __init__(self, object_detection_handle) -> None:
        self.handle: DeploymentHandle = object_detection_handle.options(
            use_new_handle_api=True,
        )

    @app.get("/detect")
    async def detect(self, image_url: str):
        result = await self.handle.detect.remote(image_url)
        return JSONResponse(content=result)


@serve.deployment(
    autoscaling_config={"min_replicas": 1, "max_replicas": 2},
)
class ObjectDetection:
    def __init__(self):
        self.model = YOLO('yolov8n.pt')

    async def detect(self, image_url: str):
        results = self.model(image_url)

        detected_objects = []
        if len(results) > 0:
            for result in results:
                for box in result.boxes:
                    class_id = int(box.cls[0])
                    object_name = result.names[class_id]
                    coords = box.xyxy[0].tolist()
                    detected_objects.append({"class": object_name, "coordinates": coords})

        if len(detected_objects) > 0:
            return {"status": "found", "objects": detected_objects}
        else:
            return {"status": "not found"}

entrypoint = APIIngress.bind(ObjectDetection.bind())
