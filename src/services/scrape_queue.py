import queue
import threading
import time
from utils.singleton import Singleton

TIME_TO_THROTTLE = 5


class ScrapeQueue(metaclass=Singleton):
    def __init__(self):
        self.queue = queue.Queue(500)

    def run(self):
        while True:
            # check for empty and sleep
            task = self.queue.get()
            task.process_task()
            time.sleep(TIME_TO_THROTTLE)
            self.queue.task_done()

    def add(self, func, *args):
        # check for full, log, skip
        self.queue.put(ScrapeTask(func, *args))


class ScrapeTask():
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def process_task(self):
        self.func(*self.args)
