from task_list import TaskList


def int_input(prompt, min_val, max_val):
    while True:
        try:
            val = int(input(prompt))
            if val < min_val or val > max_val:
                print(f"Please input a value between {min_val} and {max_val}")
                continue
            return val
        except ValueError:
            print("Please input a valid integer!")


def prompt_menu():
    print(
        "Menu:\n0: Create Task\n1: Edit Task\n2: Complete Task\n3: Delete Task\n4: List Tasks\n5: Quit\n"
    )

    return int_input("Input the number of the task you would like to get\n:> ", 0, 5)


def main():
    task_list = TaskList()
    while True:
        choice = prompt_menu()
        match choice:
            case 0:
                name = input("Input name of task: ")
                desc = input("Input description of task: ")
                due_date = input("Input the due date: ")
                task_list.create_task(name, desc, due_date)

            case 1:
                if len(task_list.tasks) == 0:
                    print("You don't have any tasks to edit!")
                    continue

                id = int_input(
                    "Input the id of the task\n:> ", 0, len(task_list.tasks) - 1
                )

                name = input("Input name of task: ")
                desc = input("Input description of task: ")
                due_date = input("Input the due date: ")

                task_list.update(id, name, desc, due_date)

            case 2:
                if len(task_list.tasks) == 0:
                    print("You don't have any tasks to complete!")
                    continue

                id = int_input(
                    "Input the id of the task\n:> ", 0, len(task_list.tasks) - 1
                )

                complete = False
                val = input(
                    "Would you like to set this task to complete, or incomplete C: Complete, Anything Else: Not-Complete"
                ).lower()
                if val == "c":
                    complete = True

                task_list.complete(id, complete)

                continue

            case 3:
                if len(task_list.tasks) == 0:
                    print("You don't have any tasks to delete!")
                    continue

                id = int_input(
                    "Input the id of the task\n:> ", 0, len(task_list.tasks) - 1
                )

                print("Are you sure? <Y/n>")
                val = input()
                if val != "Y":
                    print("Not Deleting Task")
                    continue

                print("Deleting Task")

                task_list.delete_task(id)

            case 4:
                completed = input(
                    "Should the viewed tasks be completed\nY: Yes\nN: No\nAnything Else: Show All Tasks\n:> "
                )
                if completed.lower() == "y":
                    print(task_list.filter_task(True))
                elif completed.lower() == "n":
                    print(task_list.filter_task(False))
                else:
                    print(task_list.view_tasks())

            case 5:
                break

            case _:
                pass


if __name__ == "__main__":
    main()
