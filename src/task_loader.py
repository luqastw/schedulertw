from pathlib import Path
from src.model import Task
import json

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
TASK_FILE = DATA_DIR / "task.json"

def load_tasks(path=TASK_FILE):
    path = Path(path)

    if not path.exists():
        print("JSON not found. Creating your JSON...")

        template = Task(
            name = "Send demand email to our distributors.",
            description = "Request an new group of endoskeletons.",
            schedule = "tomorrow at 14:00",
            action = "send email",
            params = {"Henry": "hemilly83@gmail.com", "Afton": "aftonrobotics@gmail.com"},
            enable = True
        )

        path.parent.mkdir(exist_ok=True, parents=True)

        with path.open("w", encoding="utf-8") as f:
            json.dump([template.model_dump()], f, indent=4, ensure_ascii=False)
        
        return [template.model_dump()]

    with TASK_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)
         
    tasks = [Task(**item) for item in data]

    if not isinstance(tasks, list):
        raise ValueError("The JSON file should have a dict of tasks.")

    return tasks