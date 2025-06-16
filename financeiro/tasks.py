from celery import shared_task

@shared_task
def add(x, y):
    import time
    time.sleep(5)
    print('terminou')
    return 2/0

@shared_task
def send_email(email):
    return False
