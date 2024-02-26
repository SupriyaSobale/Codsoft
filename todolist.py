tasks = []

def add_task():
    task_name = input("Enter task name: ")
    tasks.append({'task_name': task_name, 'completed': False})
    print("Task added successfully")

def view_tasks():
    if not tasks:
        print("No tasks in the list")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{index + 1}. {task['task_name']} - {status}")

def mark_task_completed():
    view_tasks()
    task_index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print("Task marked as completed")
    else:
        print("Invalid task number")

def delete_task():
    view_tasks()
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task deleted successfully")
    else:
        print("Invalid task number")

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_task_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
