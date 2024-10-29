from task_creator import TaskCreator
from task import Task
from task_deleter import TaskDeleter
from task_viewer import TaskViewer

class TaskList(TaskCreator, TaskDeleter, TaskViewer):
    def __init__(self):
        self.tasks = []

    def create_task(self, name, desc, due_date):
        self.tasks += [Task(name, desc, due_date, False)]
    
    def delete_task(self, id):
        del self.tasks[id]

    def view_tasks(self):
        res = ""
        for i in range(len(self.tasks)):
            res += f"{i}: {self.tasks[i]}\n"
            return res
