class Task:
    def __init__(self, name, description, due_date, completed):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def __repr__(self):
        return f"{self.name}, {self.description}, {self.due_date}, {self.completed}"