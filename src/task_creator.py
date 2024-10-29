from abc import ABC, abstractmethod


class TaskCreator(ABC):
    @abstractmethod
    def create_task(self, name, desc, due_date): ...
