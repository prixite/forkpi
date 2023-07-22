#!/usr/bin/env bash
cd /opt/code
set -o allexport
source .env
set +o allexport

/usr/local/bin/python manage.py send_sms
