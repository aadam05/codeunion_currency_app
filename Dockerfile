FROM python:3.11

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get -y install cron \
    && apt-get -y install systemctl

WORKDIR /opt/currency_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE 'core.settings'

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .