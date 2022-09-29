FROM python:3.9.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update \
    && apt-get install -y \
        build-essential \
        ca-certificates \
        curl \
        dirmngr \
        fonts-noto-cjk \
        gcc \
        gnupg \
        libldap2-dev \
        libpq-dev \
        libsasl2-dev \
        libssl-dev \
        netcat \
        node-less \
        npm \
        python-dev \
    && rm -rf /var/lib/apt/lists/*

RUN useradd --user-group --no-create-home --no-log-init --shell /bin/bash odoo \
        && mkdir -p /opt /opt/pythonpath


WORKDIR /opt

COPY docker/docker-init.sh /docker-init.sh
RUN chmod +x /docker-init.sh

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY . .

RUN cd /opt && chown -R odoo:odoo * && npm install -g rtlcss && pip install --upgrade pip && pip install --upgrade -r /opt/requirements.txt

USER odoo

ENTRYPOINT ["/entrypoint.sh"]
