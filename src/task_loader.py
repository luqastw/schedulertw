from pathlib import Path
import json

BASE = Path(__file__).parent.parent
DATA_DIR = BASE / "data"
DATA_DIR.mkdir(exist_ok=True)
TASK_FILE = DATA_DIR / "task.json"

def ensure_task_file(path="task.json"):
    path = Path(path)

    if not path.exists():
        with path.open("w", encoding="utf-8") as f:
            json.dump([], f, ident=4)

ensure_task_file(TASK_FILE)

with open(TASK_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)

# task = Task(**data[0])