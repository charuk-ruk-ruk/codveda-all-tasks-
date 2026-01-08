import json
import os
                                #to-do list manager
class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return []

    def save_tasks(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def add_task(self, description):
        self.tasks.append({'task': description, 'completed': False})
        self.save_tasks()
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\nTo-Do List:")
        for index, task in enumerate(self.tasks):
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{index + 1}. {status} {task['task']}")
        print()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"Task '{removed['task']}' deleted.")
        else:
            print("Invalid task number.")

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            self.save_tasks()
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

def main():
    manager = TaskManager()

    while True:
        print("\n--- To-Do Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            desc = input("Enter task description: ")
            if desc.strip():
                manager.add_task(desc.strip())
            else:
                print("Task description cannot be empty.")
        
        elif choice == '2':
            manager.view_tasks()
        
        elif choice == '3':
            manager.view_tasks()
            try:
                task_num = int(input("Enter task number to mark done: ")) - 1
                manager.mark_done(task_num)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '4':
            manager.view_tasks()
            try:
                task_num = int(input("Enter task number to delete: ")) - 1
                manager.delete_task(task_num)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

                                #thank you