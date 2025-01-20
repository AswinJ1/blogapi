#!/bin/bash

# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files

# Apply database migrations
python manage.py migrate
