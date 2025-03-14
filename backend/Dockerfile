FROM python:3.10.2-slim

RUN apt update && apt upgrade -y

# set working directory
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV production
ENV APP_SETTINGS project.config.ProductionConfig
ENV SECRET_KEY my_precious

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app

RUN adduser --disabled-login app
USER app

CMD ["python", "run.py"]