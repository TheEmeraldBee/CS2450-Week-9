from abc import ABC, abstractmethod

class TaskDeleter(ABC):
    @abstractmethod
    def delete_task(self, id): ...