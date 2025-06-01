FROM python:3.10.2-slim

# set working directory
WORKDIR /app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_ENV=production

COPY . /app

RUN pip install -r requirements.txt

RUN chmod 755 /app/app/services/mail_service.py

RUN adduser --disabled-login app
USER app

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]