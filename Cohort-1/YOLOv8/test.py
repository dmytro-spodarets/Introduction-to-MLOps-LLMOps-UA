import cv2
import numpy as np
import requests
import json

image_url = "https://mlyn.by/wp-content/uploads/2023/03/4-4.jpg"
server_url = "http://3.15.175.158:8000/detect"

resp = requests.get(image_url)
image_nparray = np.asarray(bytearray(resp.content), dtype=np.uint8)
image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)

resp = requests.get(f"{server_url}?image_url={image_url}")
detections = resp.json()["objects"]

for item in detections:
    class_name = item["class"]
    coords = item["coordinates"]

    cv2.rectangle(image, (int(coords[0]), int(coords[1])), (int(coords[2]), int(coords[3])), (0, 255, 0), 2)

    cv2.putText(image, class_name, (int(coords[0]), int(coords[1] - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.imwrite("output.jpeg", image)
