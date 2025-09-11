from celery import shared_task


@shared_task
def divide(x, y):
    import time
    print('shared task')

    time.sleep(5)
    return x / y
