release: npm install --prefix frontend && npm run build --prefix frontend && python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn amm.wsgi