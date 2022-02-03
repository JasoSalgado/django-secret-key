release: python manage.py migrate
web: gunicorn main.wsgi --log-file -
worker: python manage.py rqworker default