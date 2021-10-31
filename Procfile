release: python manage.py migrate
wed: daphne django_notification.asgi:application --port $PORT --bind 0.0.0.0 -v2