import time

from celery import Celery

app = Celery('hello', broker='amqp://guest@localhost//')


@app.task
def hello():
    print("sleep for 3 seconds")
    time.sleep(3)
    print('hello world')
