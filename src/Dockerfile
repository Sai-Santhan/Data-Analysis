# Dockerfile for Django Applications

# Base image
FROM amd64/python:3.10-slim

# Python Interpreter Flags
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# Compiler and OS libraries
RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential \
    python3-dev \
    python3-setuptools

# create a directory and move into it
WORKDIR /app

# copy only the requirements
COPY ./requirements.txt /app

# Create a virtual environment in /opt & upgrade pip and install requirements
RUN python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install pip --upgrade \
    && /opt/venv/bin/pip install --no-cache-dir -r /app/requirements.txt \
    && apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* 

# copy everything
COPY . /app

# make entry point executable
RUN chmod +x entrypoint.sh

# run entrypoint
CMD [ "/app/entrypoint.sh" ]

