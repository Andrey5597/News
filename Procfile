release: python manage.py migrate --no-input
release: python manage.py crontab add

web: gunicorn news_board.wsgi