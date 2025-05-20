#!/bin/bash

# Install Python packages
pip install -r requirements.txt

# Create necessary directories
mkdir -p media/services/icons
mkdir -p static/images

# Copy service icons to media directory
cp static/images/*.png media/services/icons/ 2>/dev/null || true

# Make migrations
python manage.py makemigrations
python manage.py migrate

# Load initial data
python manage.py loaddata education_portal/fixtures/initial_data.json

# Run server
python manage.py runserver 0.0.0.0:8000
