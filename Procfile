web: python manage.py migrate --noinput && python manage.py collectstatic --noinput && daphne thehichannel.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker -v2
