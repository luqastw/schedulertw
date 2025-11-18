from pydantic import BaseModel

class Task(BaseModel):
    name: str
    description: str
    schedule: str
    action: str
    enable: bool = True