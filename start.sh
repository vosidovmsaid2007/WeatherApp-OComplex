#!/bin/sh

echo "Migration..."
python manage.py migrate

echo "Running tests..."
python manage.py test

echo "Starting server"
python manage.py runserver 0.0.0.0:8000
