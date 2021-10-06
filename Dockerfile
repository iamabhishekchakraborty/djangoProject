# syntax=docker/dockerfile:1
# pull official base image
FROM python:3.8.6-alpine

# set environment variables
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1
ENV DJANGO_DEBUG=False

# set work directory
WORKDIR /app

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# collect static files
# RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D abhishek
USER abhishek

# run gunicorn ($PORT variable. Essentially, any web server that runs on the Container Runtime must listen for HTTP traffic at the $PORT environment variable, which is set by Heroku at runtime.)
# CMD gunicorn djangoproject.wsgi:application --bind 0.0.0.0:$PORT
