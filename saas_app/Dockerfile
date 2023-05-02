FROM python:3.8-slim-buster@sha256:bf7fc227b0dc580c8bbbe696b61840c61bc241b404a288ef1612ce11fe92ab85

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
