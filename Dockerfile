FROM ubuntu:24.04

RUN apt update && \
    apt install -y python3 python3-pip python3-flask

WORKDIR /app

COPY . /app

CMD ["python3", "app.py"]
