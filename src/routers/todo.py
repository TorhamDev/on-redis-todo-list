from fastapi import APIRouter, Body, Depends, status
from src.db._redis import get_db
from redis import Redis
from src.utils.jwt import JWTHandler
from src.schemas.jwt import JWTPayload
from src.schemas._input import CreateTodoInput
from src.controllers.todo import TodoController



router = APIRouter(tags=["todo"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_todo(
    user_info: JWTPayload = Depends(JWTHandler.verify_token),
    data: CreateTodoInput = Body(),
    db: Redis = Depends(get_db),

):
    data = TodoController(db).create_todo(username=user_info.username, todo_data=data)
    
    return data


@router.get("/")
def get_all_todos():
    ...

@router.get("/{todo_id}/")
def get_a_todo():
    ...

@router.put("/{todo_id}")
def update_a_todo():
    ...