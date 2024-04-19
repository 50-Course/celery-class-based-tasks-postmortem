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

# TODO: Test for leakage behavior in function-based tasks
# to verify behavior only occurs in C.B.T

my_task = app.register_task(MyTask)
my_task.delay()
my_task.delay()
assert len(my_task.run()) == 1, "Error it appears there are leaks"
