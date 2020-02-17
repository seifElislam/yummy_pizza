#!/bin/sh

echo " >> installing dev requirements"
pip install -r /app/requirements/dev.txt
echo " >> starting app"
python /app/manage.py makemigrations
python /app/manage.py migrate
python /app/manage.py loaddata admin.json
python /app/manage.py runserver 0.0.0.0:8000
