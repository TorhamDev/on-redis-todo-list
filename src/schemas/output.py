from pydantic import BaseModel

class TodoDetailsOutput(BaseModel):
    id: str
    title: str
    details: str