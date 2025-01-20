#!/bin/bash

# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Start the application with Gunicorn
gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT
