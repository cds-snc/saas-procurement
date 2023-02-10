# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

# Install packages
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get autoremove -y \
    && apt-get clean -y 

COPY ./apt-packages.txt ./
RUN apt-get update && apt-get install -y $(cat apt-packages.txt)

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
RUN pip install --upgrade pip
COPY ./saas_app/requirements_dev.txt .
RUN python -m pip install -r requirements_dev.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "saas_app.saas_app.wsgi"]
