#!/bin/sh

# Make database migrations
echo "Make database migrations"
python3 manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate