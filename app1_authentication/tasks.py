# feedback/tasks.py

from celery import shared_task


@shared_task
def kaka():
    print("it is working")
