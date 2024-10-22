
def delete(arrayToEdit):
    """Deletes a task based on the Index of the task."""

    #get input and convert to integer
    taskToDelete = int(input("Task number that you want to delete: "))

    #account for the fact that arrays/lists start from 0
    taskToDelete -= 1

    #delete the array/list index based on user input using the built-in del functionality
    del arrayToEdit[taskToDelete]