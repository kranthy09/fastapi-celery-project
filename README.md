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

## Retry Failed Tasks:

### 1. Task Retry Decorator

```python
@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 7, "countdown": 5})
def task_process_notification(self):
if not random.choice([0, 1]): # mimic random error
raise Exception()

    requests.post("https://httpbin.org/delay/5")
```

- autoretry_for takes a list/tuple of exception types that you'd like to retry for.
- retry_kwargs takes a dictionary of additional options for specifying how autoretries
  are executed. In the above example, the task will retry after a 5 second delay (via countdown)
  and it allows for a maximum of 7 retry attempts (via max_retries). Celery will stop
  retrying after 7 failed attempts and raise an exception.

### 2. Exponential Backoff

If your Celery task needs to send a request to a third-party service, it's a good idea to use exponential backoff to avoid overwhelming the service.

Celery supports this by default:

```python
@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5})
def task_process_notification(self):
    if not random.choice([0, 1]):
        # mimic random error
        raise Exception()

    requests.post("https://httpbin.org/delay/5")
```

You can also set retry_backoff to a number for use as a delay factor

To prevent thundering herd, celery has you covere here with `retry_jitter`. This option is set `true` by default to prevent thundering herd problem when you use celery's built-in `retry_backoff`
