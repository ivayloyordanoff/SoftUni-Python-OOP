from abc import ABC, abstractmethod


class AbstractWorker(ABC):

    @abstractmethod
    def work(self):
        pass


class Worker(AbstractWorker):

    def work(self):
        print("I'm working!!")


class SuperWorker(AbstractWorker):

    def work(self):
        print("I work very hard!!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractWorker), f"`worker` must be of type {Worker}"

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()
