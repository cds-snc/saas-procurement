FROM mcr.microsoft.com/devcontainers/python:0-3.11@sha256:452e43dd2381de67191c53f7692433baba156ee9138ccfaed5124ff26c63eaed

# Install packages
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get autoremove -y \
    && apt-get clean -y 

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# upgrade pip
RUN pip install --upgrade pip
# copy requirements files and install them
COPY saas_app/requirements.txt saas_app/requirements_dev.txt tmp/pip-tmp/
RUN pip install -r /tmp/pip-tmp/requirements.txt \
    pip install -r /tmp/pip-tmp/requirements_dev.txt

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends cron 



