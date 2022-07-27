web: python manage.py runserver 0.0.0.0:$PORT
worker1: celery -A demo worker -l info -P eventlet
worker2: celery -A demo beat -l info -S django
release: python manage.py migrate