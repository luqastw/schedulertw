from pydantic import BaseModel
from typing import Dict, Any

class Task(BaseModel):
    name: str
    description: str
    schedule: str
    action: str
    params: Dict[str, Any]
    enable: bool = True