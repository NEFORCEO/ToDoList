

from pydantic import BaseModel


class CreateTask(BaseModel):
    title: str 
    task_name: str 