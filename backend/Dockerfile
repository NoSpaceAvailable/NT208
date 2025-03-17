FROM python:3.10.2-slim

RUN apt update && apt upgrade -y

# set working directory
WORKDIR /

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV production
ENV SECRET_KEY lmao_hahaha

COPY . /
RUN pip install -r requirements.txt

RUN adduser --disabled-login app
USER app

CMD ["python", "run.py"]