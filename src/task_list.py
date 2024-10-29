from task_creator import TaskCreator
from Task import Task


class TaskList(TaskCreator):
    def __init__(self):
        self.tasks = []

    def create_task(self, name, desc, due_date):
        self.tasks += [Task(name, desc, due_date, False)]
