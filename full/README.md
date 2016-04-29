Dorothy Cargo Bikes
========================================================


Deploy to Production
--------------------------------------------------------

We are using Docker and Docker-Compose.

To deploy to staging just:

1 - docker-compose -f staging.yml build # Install requirements

2 - docker-compose -f staging.yml up -d --force-recreate # Start production server

To deploy to production just:

1 - docker-compose build # Install requirements

2 - docker-compose up -d --force-recreate # Start production server

```
# Compose up will do the following:
 - makemigrations
 - migrate
 - collectstatic
 - start gunicorn
 - start services like celery for example
```

Useful commands
--------------------------------------------------------

Stop docker services:
- docker-compose stop

Check if services are running:
- docker-compose ps
- docker ps

Logging:
- docker logs dorothybackend_dorothy_nginx_1
- docker-compose logs dorothy_web
- docker-compose logs dorothy_postgis
- docker-compose logs dorothy_redis

Enter docker container to Run Commands:
- docker-compose run --rm dorothy_web bash

Backup DB:
- python3 manage.py dbbackup --settings=dorothy.settings.staging

Enter Postgres DB inside container:
- python3 manage.py dbshell --settings=dorothy.settings.staging