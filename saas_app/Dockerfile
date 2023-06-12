FROM python:3.8-slim-buster@sha256:66aba636613bb50b6b5e2fbd497ed7c90ea0eeacb06d8ab6dcf673f3ddd4c872

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
