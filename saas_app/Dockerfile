FROM python:3.8-slim-buster@sha256:89ad1c2cd09bda5bc85ada7eb93b5db57d32dc0105b7c942d272d68f376f67c3

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
