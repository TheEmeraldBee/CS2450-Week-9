from abc import ABC, abstractmethod

class TaskEditor(ABC):
    @abstractmethod
    def update(self, id, name, description, due_date): ...

    @abstractmethod
    def complete(self,id,completed): ...
