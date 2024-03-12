from pydantic import BaseModel

class TodoDetailsOutput(BaseModel):
    id: str
    title: str
    details: str

class TodoSimpleOutput(BaseModel):
    id: str
    title: str

class TodoListDetailsOutput(BaseModel):
    todos: list[TodoSimpleOutput]

