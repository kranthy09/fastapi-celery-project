# fastapi-celery-project

## Commands(local development)

docker run -p 6379:6379 --name some-redis -d redis

uvicorn main:app --reload

celery -A main.celery worker --loglevel=info

celery -A main.celery flower --port=5555
