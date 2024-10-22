def filter(tasks, completed: bool | None = None):
    if completed is None:
        return tasks

    new_tasks = []

    for task in tasks:
        if task.status == completed:
            new_tasks += [task]

    return new_tasks
