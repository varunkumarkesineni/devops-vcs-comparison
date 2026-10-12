"""Simple command-line task manager used as the sample project.

The same code base is hosted on GitHub, GitLab and Bitbucket so that the
platforms can be compared fairly (repositories, branching, pull/merge
requests, issues and CI/CD pipelines).
"""
import json
import sys
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks(path=DATA_FILE):
    if not Path(path).exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks, path=DATA_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, title):
    if not title or not title.strip():
        raise ValueError("Task title cannot be empty")
    task = {"id": len(tasks) + 1, "title": title.strip(), "done": False}
    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    raise KeyError(f"Task {task_id} not found")


def list_tasks(tasks, only_pending=False):
    return [t for t in tasks if not (only_pending and t["done"])]


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        print("Usage: taskmanager.py add <title> | done <id> | list")
        return 1
    tasks = load_tasks()
    command = argv[0]
    if command == "add":
        task = add_task(tasks, " ".join(argv[1:]))
        save_tasks(tasks)
        print(f"Added task {task['id']}: {task['title']}")
    elif command == "done":
        task = complete_task(tasks, int(argv[1]))
        save_tasks(tasks)
        print(f"Completed task {task['id']}")
    elif command == "list":
        for t in list_tasks(tasks):
            mark = "x" if t["done"] else " "
            print(f"[{mark}] {t['id']}. {t['title']}")
    else:
        print(f"Unknown command: {command}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
