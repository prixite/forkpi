#!/usr/bin/env bash
docker-compose build
docker-compose up -d
docker-compose exec forkpi ./manage.py migrate
docker-compose exec forkpi ./manage.py collectstatic --noinput;
docker-compose ps
