from abc import ABC, abstractmethod

class TaskViewer(ABC):
    @abstractmethod
    def edit_task(self, name, desc, due_date, completed):
        pass

    @abstractmethod
    def complete_task(self, completed):
        pass