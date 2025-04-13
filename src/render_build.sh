#!/usr/bin/env bash
# Install dependencies, run migrations, and collect static files

pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput