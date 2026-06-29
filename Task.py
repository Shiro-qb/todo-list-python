from datetime import datetime

class Task:
    def __init__(self, title, completed, start_date, deadline):
        self.title = title
        self.completed = completed
        self.start_date = start_date
        self.deadline = deadline

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} | Start: {self.start_date} | Deadline: {self.deadline}"

def create_task():
    while True:
        title = input("Enter Task Title: ")
        start_date = input("Enter Task Start Date: ")
        deadline = input("Enter Task Deadline: ")
        task = Task(title, False, start_date, deadline)
        return task

def enumerate_tasks():
    if not tasks:
        print("No tasks yet")
        return

    print("List of tasks")
    for i in range(1, len(tasks) + 1):
        print(f"{i}. {tasks[i - 1]}")

def complete_task():
    while True:
        new = input("Have you completed a task? (Y/N): ")
        if new == "Y":
            completed = int(input("Enter Task number: "))
            if completed > len(tasks):
                print("Invalid task")
            else:
                tasks[completed - 1].completed = True
                print(tasks[completed - 1])
                print("Way to go!")
        elif new == "N":
            print("Thank You")
            break
        else:
            print("Invalid input")


def delete_task():
    enumerate_tasks()
    again = True
    while again:
        task_to_delete = int(input("Enter Task Number: "))
        if task_to_delete > len(tasks):
            print("Invalid task")
            continue
        else:
            deleted = tasks[task_to_delete-1].title
            tasks.pop(task_to_delete - 1)
            print(f"'{deleted}' has been successfully deleted")
            enumerate_tasks()
            again = input("Press Enter to finish and any key to delete a new task:")






tasks = []
while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Quit")
    choice = input("Pick an option: ")
    if choice == "1":
        new_task = create_task()
        tasks.append(new_task)
        print("Task added!")
    elif choice == "2":
        enumerate_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break

