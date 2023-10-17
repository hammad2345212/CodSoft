from task import Task
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"Task {i}:\n{task}\n")

    def mark_task_as_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.mark_as_completed()
            print(f"Task '{task.title}' has been marked as completed.")
        else:
            print("Invalid task number. Please try again.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task.title}' has been removed from the list.")
        else:
            print("Invalid task number. Please try again.")

def main():
    todo_list = ToDoList()

    while True:
        print("What would you like to do?")
        print("1. Add a new task")
        print("2. View tasks")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_task_as_completed(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_index)
        elif choice == "5":
            print("Goodbye! Have a productive day.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
