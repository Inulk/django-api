# django-apis project

### Build docker
docker build .
docker compose build 

### list volumes in docker
docker volume ls

### remove volume inside docker
deocker volume rm name_of_the_volume

docker compose up
docker compose run --rm web python manage.py

### Run tests
docker compose run --rm app python manage.py test

### Impliment DB
- configure database connection
- python manage.py makemigrations

### creating superuser 
docker compose run --rm app python manage.py createsuperuser

### create new app in django
python manage.py startapp user

