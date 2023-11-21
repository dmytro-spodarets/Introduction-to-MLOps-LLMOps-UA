#!/bin/bash
export WANDB_API_KEY="xxx"

pip install -r requirements.txt
pip install -U ultralytics "ray[tune]"

python yolov8.py