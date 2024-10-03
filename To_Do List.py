import json

# Empty list to store tasks, which will be loaded from file
todo_list = []

def add_task(task):
    """Adds a new task to the todo list."""
    todo_list.append(task)
    print(f'Task "{task}" added!')

def view_tasks():
    """Displays all tasks in the todo list."""
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("Tasks in the list:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def remove_task(index):
    """Removes a task from the todo list by its index."""
    try:
        removed_task = todo_list.pop(index - 1)
        print(f'Task "{removed_task}" removed!')
    except IndexError:
        print("Invalid index. Please try again.")

def save_tasks_to_file(tasks, filename="todo_list.json"):
    """Saves the current tasks to a JSON file."""
    try:
        with open(filename, "w") as file:
            json.dump(tasks, file, indent=4)
        print(f"Tasks successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving tasks: {e}")

def load_tasks_from_file(filename="todo_list.json"):
    """Loads tasks from a JSON file."""
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty list.")
        return []

def menu():
    """Displays a menu for the user to interact with the to-do list."""
    global todo_list
    todo_list = load_tasks_from_file()  # Load tasks when the program starts
    
    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Save and Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)

        elif choice == '2':
            view_tasks()

        elif choice == '3':
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '4':
            save_tasks_to_file(todo_list)  # Save tasks before exiting
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please try again.")

# Run the menu function to start the program
menu()