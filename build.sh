#!/bin/bash
set -o errexit  # Exit immediately if a command exits with a non-zero status

# Install dependencies
pip install -r requirements.txt  # Corrected the command to use '-r' instead of '-'



# Run database migrations
python manage.py migrate
