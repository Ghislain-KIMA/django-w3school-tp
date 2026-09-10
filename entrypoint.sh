#!/usr/bin/env bash
set -e

echo "==> Application des migrations..."
python manage.py migrate --noinput

echo "==> Seeding de la base de données..."
python manage.py seed_members

echo "==> Lancement du serveur Gunicorn..."
exec gunicorn my_tennis_club.wsgi:application --bind 0.0.0.0:$PORT