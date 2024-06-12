# Use the official Python image from the Docker Hub
FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt

RUN apt-get add --update --no-cache postgresql-client jpeg-dev
RUN apt-get add --update --no-cache --virtual .tmp-build-deps \ 
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apt-get del .tmp-build-deps

RUN mkdir /app
# COPY ./app /app
COPY myproject /app/
WORKDIR /app


CMD [ "python", "manage.py", "runserver" ]