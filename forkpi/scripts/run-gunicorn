#!/usr/bin/env bash
gunicorn --worker-tmp-dir /dev/shm project.wsgi:application --bind unix:/dev/shm/gunicorn.sock
