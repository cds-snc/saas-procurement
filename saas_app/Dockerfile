FROM python:3.8-slim-buster@sha256:8799b0564103a9f36cfb8a8e1c562e11a9a6f2e3bb214e2adc23982b36a04511

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
	postgresql \
	gcc \
	jq \
	musl-dev \
	cron

# Change working directory, copy requirements.txt and install application dependencies
WORKDIR /saas_app
COPY requirements.txt /saas_app/
RUN pip install --no-cache-dir --upgrade pip \
	&& pip install --upgrade setuptools \
	&& pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /saas_app/

#Build variables
ARG GIT_SHA
ARG BUILD_DATE
ENV GIT_SHA=$GIT_SHA
ENV BUILD_DATE=$BUILD_DATE

# Expose port and run the application
EXPOSE 8000
ENTRYPOINT ./bin/initialize.sh
