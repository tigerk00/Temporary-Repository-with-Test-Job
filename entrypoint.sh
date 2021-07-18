#!/bin/bash -x

#Flush db data
echo "Flush db data"
python manage.py flush --no-input

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate --noinput || exit 1

# Reminder
echo "[*] USE http://localhost:8000/ [*]"

exec "$@"
