# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /saas_app

# Install pip requirements
COPY requirements.txt /saas_app
RUN python -m pip install -r /saas_app/requirements.txt

COPY . /saas_app

RUN python manage.py collectstatic --noinput

# Creates a non-root user with an explicit UID and adds permission to access the /saas_app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" vscode && chown -R vscode /saas_app
USER vscode

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "saas_app.wsgi"]
