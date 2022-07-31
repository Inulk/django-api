# django-apis project

### Build docker
docker build .
docker compose build 

docker compose up
docker compose run --rm web python manage.py

## Run tests
docker compose run --rm app python manage.py test

# Impliment DB
- create database connection
- python manage.py migrate

