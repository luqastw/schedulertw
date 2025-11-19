from typing import Dict

class TaskRegistry:
    def __init__(self):
        self._tasks = {}

    def register(self, task: Dict):
        name = task.name
        if name in self._tasks:
            raise ValueError("This task already exists.")
        self._tasks[name] = task
        print(f"Task '{task.name}' registred.")

    def get_all(self):
        return list(self._tasks.values())