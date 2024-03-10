from fastapi import APIRouter, Body, Depends
from src.schemas._input import RegisterUserInput
from src.db._redis import get_db
from redis import Redis
from src.controllers.users import UserController

router = APIRouter(tags=["users"])

@router.post("/register")
def register_user(
    data : RegisterUserInput = Body(),
    db: Redis = Depends(get_db)
):
    UserController(db).register(data.username, data.password)
    return data