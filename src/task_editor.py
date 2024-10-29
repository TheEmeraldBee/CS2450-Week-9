from abc import ABC, abstractmethod

class TaskEditor(ABC):
    @abstractmethod
    def edit_name(self, id, name): ...

    @abstractmethod
    def edit_description(self,id,description): ...

    @abstractmethod
    def edit_due_date(self,id,due_date): ...

    @abstractmethod
    def edit_completed(self,id,completed): ...
