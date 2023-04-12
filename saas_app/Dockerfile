
FROM python:3.8-slim-buster@sha256:31d0d41a5356cfbb9d7a3788f6443d02a69a0f2cfa97aa8873e6fb48bbfa3ffc

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
	postgresql \
	gcc \
	jq \
	musl-dev

WORKDIR /saas_app
COPY requirements.txt /saas_app/
RUN pip install -r requirements.txt
COPY . /saas_app/
EXPOSE 8000
ENTRYPOINT ./bin/initialize.sh
