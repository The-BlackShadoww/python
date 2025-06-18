import json
import os

FILENAME = "tasks.json"

# Load existing tasks from file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

# Save current tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Display the task list
def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks yet!")
    else:
        for i, task in enumerate(tasks):
            status = "✅" if task["done"] else "❌"
            print(f"{i+1}. {status} {task['title']}")
            if task.get("note"):
                print(f"   📝 {task['note']}")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    note = input("Optional note: ")
    tasks.append({"title": title, "note": note, "done": False})
    print("🆕 Task added!")

# Mark a task as complete
def complete_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task number to complete: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            print("✅ Task marked as complete!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️ Enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"🗑️ Removed task: {removed['title']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("⚠️ Enter a valid number.")

# Menu-driven interface
def main():
    tasks = load_tasks()

    while True:
        print("\n📋 To-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("📁 Tasks saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the app
if __name__ == "__main__":
    main()
