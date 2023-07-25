FROM python:3.8-slim-buster@sha256:8799b0564103a9f36cfb8a8e1c562e11a9a6f2e3bb214e2adc23982b36a04511

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
	postgresql \
	gcc \
	jq \
	musl-dev \
	cron

WORKDIR /saas_app
COPY requirements.txt /saas_app/
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt
COPY . /saas_app/
EXPOSE 8000
ENTRYPOINT ./bin/initialize.sh
