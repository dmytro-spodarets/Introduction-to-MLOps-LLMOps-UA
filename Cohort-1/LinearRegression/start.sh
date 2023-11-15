#!/bin/sh
python download_model.py
uvicorn main:app --host 0.0.0.0 --port 5000