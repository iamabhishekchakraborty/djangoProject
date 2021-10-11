# syntax=docker/dockerfile:1
# pull official base image
FROM python:3.8.6-alpine
LABEL maintainer="abhishek"

# set environment variables
# Prevents Python from buffering stdout and stderr but send it to terminal
ENV PYTHONUNBUFFERED=1
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# create root directory and copy project
RUN mkdir /app
# set work directory
WORKDIR /app
#COPY ./requirements.txt /requirements.txt
COPY . /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# install dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
# RUN python -m venv /py && \
#     /py/bin/pip install --upgrade pip && \
#     /py/bin/pip install -r /requirements.txt && \
#     adduser --disabled-password --no-create-home abhishek

# adds the virtual environment to image path
# ENV PATH="/py/bin:$PATH"

# collect static files
# RUN python manage.py collectstatic --noinput

# run as non-root user
#RUN adduser -D abhishek
#USER abhishek

# run gunicorn ($PORT variable. Essentially, any web server that runs on the Container Runtime must listen for HTTP traffic at the $PORT environment variable, which is set by Heroku at runtime.)
# CMD gunicorn djangoproject.wsgi:application --bind 0.0.0.0:$PORT

# run entrypoint.sh script
ENTRYPOINT ["./entrypoint.sh"]