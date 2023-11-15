FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY download_model.py download_model.py
COPY main.py main.py

RUN pip install -r requirements.txt

COPY start.sh /start.sh
CMD ["/start.sh"]