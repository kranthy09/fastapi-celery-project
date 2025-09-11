# fastapi-celery-project

## Commands(local development)

```bash
docker run -p 6379:6379 --name some-redis -d redis
```

```bash
uvicorn main:app --reload
```

```bash
celery -A main.celery worker --loglevel=info
```

```bash
celery -A main.celery flower --port=5555
```
