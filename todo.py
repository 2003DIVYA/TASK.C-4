# Define an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print("Task added!")

# Function to list all tasks
def list_tasks():
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the list.")

# Function to remove a task by its index
def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid task index.")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. List tasks")
    print("3. Remove task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        index = int(input("Enter the task index to remove: "))
        remove_task(index)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")