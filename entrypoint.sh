#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
  echo "waiting for postgres..."
  while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 0.1
  done
  echo "PostgreSQL started..."
fi

# the below commands can be commented so they don't run on every container start/re-start
# instead they can be run manually after the containers spin up like
# docker-compose exec web python manage.py flush --no-input
python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate

exec "$@"
