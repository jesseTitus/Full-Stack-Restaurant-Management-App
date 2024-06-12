# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install dependencies

RUN apt-get update \
    && apt-get install -y \
    postgresql-client \
    libjpeg-dev \
    gcc \
    libc-dev \
    postgresql-server-dev-all \
    musl-dev \
    zlib1g zlib1g-dev \
    pkg-config \
    libmariadb-dev \
    libpq-dev \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Set up the application directory
RUN mkdir /app
COPY myproject /app/
WORKDIR /app


CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]