FROM --platform=linux/arm64 python:3.8

WORKDIR /usr/src/app
        
COPY . /usr/src/app

RUN pip install --upgrade pip \
        && pip install --no-cache-dir uvicorn fastapi

CMD [ "python", "./hello_world.py"]
