from abc import ABC, abstractmethod
import time


class AbstractWorkerWorkable(ABC):
    @staticmethod
    @abstractmethod
    def work():
        pass


class AbstractWorkerEatable(ABC):
    @staticmethod
    @abstractmethod
    def eat():
        pass


class Worker(AbstractWorkerWorkable, AbstractWorkerEatable):
    @staticmethod
    def work():
        print("I'm normal worker. I'm working.")

    @staticmethod
    def eat():
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(AbstractWorkerWorkable, AbstractWorkerEatable):
    @staticmethod
    def work():
        print("I'm super worker. I work very hard!")

    @staticmethod
    def eat():
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(AbstractWorkerWorkable):
    @staticmethod
    def work():
        print("I'm a robot. I'm working....")


class Manager(ABC):
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkManager(Manager):
    def set_worker(self, worker):
        if not isinstance(worker, AbstractWorkerWorkable):
            raise AssertionError(f"`worker` must subclass of type {AbstractWorkerWorkable}")

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(Manager):
    def set_worker(self, worker):
        if not isinstance(worker, AbstractWorkerEatable):
            raise AssertionError(f"`worker` must subclass of type {AbstractWorkerEatable}")

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()
work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()
work_manager.set_worker(Robot())
work_manager.manage()

try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass
