import celery
from celery import Celery

app = Celery('task', broker='redis://localhost:6379/0')

class MyTask(celery.Task):
    def __init__(self):
        self.my_list = []

    def run(self, *args, **kwargs):
        self.my_list.append(1)
        print(self.my_list)
        assert len(self.my_list) == 1

my_task = app.register_task(MyTask)
my_task.delay()
my_task.delay()
