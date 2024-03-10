from pydantic import BaseModel


class RegisterUserInput(BaseModel):
    username: str
    password: str
