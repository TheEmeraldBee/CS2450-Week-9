from task_creator import TaskCreator
from task import Task
from task_deleter import TaskDeleter


class TaskList(TaskCreator, TaskDeleter):
    def __init__(self):
        self.tasks = []

    def create_task(self, name, desc, due_date):
        self.tasks += [Task(name, desc, due_date, False)]
    
    def delete_task(self, id):
        del self.tasks[id]

