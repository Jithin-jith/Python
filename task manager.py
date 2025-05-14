import os

TODO_FILE = "todo.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks in your list!")
        return
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Manager:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input("Enter new task: ").strip()
            tasks.append(task)
            save_tasks(tasks)
            print("Task added.")
        elif choice == "3":
            show_tasks(tasks)
            idx = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx] = f"[Done] {tasks[idx]}"
                save_tasks(tasks)
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        elif choice == "4":
            show_tasks(tasks)
            idx = int(input("Enter task number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                removed = tasks.pop(idx)
                save_tasks(tasks)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()