from celery import shared_task
from celery.contrib import rdb


@shared_task
def divide(x, y):
    # rdb.set_trace()

    import time

    time.sleep(5)
    return x / y
