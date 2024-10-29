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

    def filter_task(self, completed):
        res = ""
        for i in range(len(self.tasks)):
            if self.tasks[i].completed == completed:
                res += f"{i}: {self.tasks[i]}\n"
        return res
    
    def update(self, id, name, desc, due_date):
        self.tasks[id].name = name
        self.tasks[id].description = desc
        self.tasks[id].due_date = due_date

    def complete(self, id, completed):
        self.tasks[id].completed = completed