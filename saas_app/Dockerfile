FROM python:3.8-slim-buster@sha256:f2199258d29ec06b8bcd3ddcf93615cdc8210d18a942a56b1a488136074123f3

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    ca-certificates \
    curl \
    git \
    gstreamer1.0-libav \
    libnss3-tools \
    libatk-bridge2.0-0 \
    libcups2-dev \
    libxkbcommon-x11-0 \
    libxcomposite-dev \
    libxrandr2 \
    libgbm-dev \
    libgtk-3-0 \
    libxshmfence-dev \
    gnupg2 \
    postgresql-client \
    openssh-client \
    python3-pip \
    unzip \
    vim \
    wget \
    xz-utils \
    zsh \
    entr \
    && apt-get autoremove -y \
    && apt-get clean -y

WORKDIR /saas_app

# Set build variables
ARG git_sha
ENV GIT_SHA=$git_sha

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /saas_app

COPY initialize.sh /saas_app/initialize.sh

ENTRYPOINT [ "/saas_app/initialize.sh" ]