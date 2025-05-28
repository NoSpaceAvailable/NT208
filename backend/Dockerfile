FROM python:3.10.2-slim

# set working directory
WORKDIR /app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app/app:$PYTHONPATH
ENV FLASK_ENV production
ENV SECRET_KEY lmao_hahaha

COPY . /app
RUN pip install -r requirements.txt

RUN chmod 755 /app/app/services/mail_service.py

RUN adduser --disabled-login app
USER app

CMD ["python", "run.py"]