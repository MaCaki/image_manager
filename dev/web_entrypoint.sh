#!/bin/bash

pushd /home/image_manager/

# Collect static files
echo "Collect static files"
python3 manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate

python3 manage.py runserver 0.0.0.0:8000
