from fastapi import APIRouter, Body, Depends
from src.schemas._input import LoginInput
from src.db._redis import get_db
from redis import Redis
from src.controllers.users import UserController

router = APIRouter(tags=["users", "login"])

@router.post("/")
def login_user(
    data : LoginInput = Body(),
    db: Redis = Depends(get_db)
):
    token = UserController(db).login(data.username, data.password)
    return token