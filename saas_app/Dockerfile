FROM python:3.8-slim-buster@sha256:eb48d017c5e117d9fbcbe991b4dbc61339734e01578d8d350b38fe2033a67199

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
