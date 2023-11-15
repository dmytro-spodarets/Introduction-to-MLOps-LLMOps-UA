import wandb
import ray

from ultralytics import YOLO
from datetime import datetime

current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

run = wandb.init(project='YOLOv8x', name=f'YOLOv8x-coco8_{current_datetime}')
ray.init()
model = YOLO("yolov8n.pt")

model.train(data="coco8.yaml", epochs=1)
metrics = model.val()
results = model("https://ultralytics.com/images/bus.jpg")
success = model.export()

run.finish()