from fastapi import APIRouter, Body, Depends, status
from src.db._redis import get_db
from redis import Redis
from src.utils.jwt import JWTHandler
from src.schemas.jwt import JWTPayload
from src.schemas._input import CreateTodoInput
from src.schemas.output import TodoListDetailsOutput
from src.controllers.todo import TodoController



router = APIRouter(tags=["todo"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_todo(
    user_info: JWTPayload = Depends(JWTHandler.verify_token),
    data: CreateTodoInput = Body(),
    db: Redis = Depends(get_db),

):
    data = TodoController(db).create(username=user_info.username, todo_data=data)
    
    return data


@router.get("/", response_model=TodoListDetailsOutput)
def get_all_todos(
    user_info: JWTPayload = Depends(JWTHandler.verify_token),
    db: Redis = Depends(get_db),

):
    data = TodoController(db).get_all(username=user_info.username)
    
    return data


@router.get("/{todo_id}/")
def get_a_todo(
    todo_id: str,
    user_info: JWTPayload = Depends(JWTHandler.verify_token),
    db: Redis = Depends(get_db),
):
    data = TodoController(db).get_one(username=user_info.username, todo_id=todo_id)

    return data


@router.put("/{todo_id}")
def update_a_todo():
    ...


@router.delete("/{todo_id}")
def delete_a_todo():
    ...