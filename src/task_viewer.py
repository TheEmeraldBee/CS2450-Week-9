from abc import ABC, abstractmethod

class TaskViewer(ABC):
    @abstractmethod
    def view_tasks(self):
        pass

    @abstractmethod
    def filter_task(self, completed):
        pass