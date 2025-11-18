from src.task_loader import TASK_FILE

class TaskRegistry:
    def __init__(self):
        self.tasks = {}

    def register(self, task):
        self.tasks[task.name] = task

# TaskRegistry.register(TASK_FILE)