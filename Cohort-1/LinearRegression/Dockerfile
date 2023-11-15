FROM pytorch/manylinux-cpu:latest

ARG WANDB_API_KEY
ENV WANDB_API_KEY=$WANDB_API_KEY

WORKDIR /app

COPY requirements.txt requirements.txt
COPY download_model.py download_model.py
COPY main.py main.py

RUN pip install -r requirements.txt
RUN python download_model.py

COPY start.sh /start.sh
CMD ["/start.sh"]
