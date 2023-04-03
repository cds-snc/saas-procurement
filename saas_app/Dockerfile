FROM arm64v8/python:3.11.2-slim@sha256:474f1e977c7dcc3c47ee9fee5d50764763c111f7ce8a0ce2282638fdf6135919

RUN  apt-get update \
  && apt-get install -y make

WORKDIR /saas_app

# Set build variables
ARG git_sha
ENV GIT_SHA=$git_sha

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /saas_app

COPY initialize.sh /saas_app/initialize.sh

ENTRYPOINT [ "/saas_app/initialize.sh" ]