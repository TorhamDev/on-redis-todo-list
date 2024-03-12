from pydantic import BaseModel


class RegisterUserInput(BaseModel):
    username: str
    password: str


class LoginInput(BaseModel):
    username: str
    password: str

class UpdateUserInput(BaseModel):
    new_username: str


class CreateTodoInput(BaseModel):
    title: str
    details: str