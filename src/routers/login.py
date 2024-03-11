from fastapi import APIRouter, Body, Depends
from src.schemas._input import LoginInput
from src.db._redis import get_db
from redis import Redis
from src.controllers.users import UserController
from src.schemas.jwt import JWTPayload

router = APIRouter(tags=["users", "login"])

@router.post("/", response_model=JWTPayload)
def login_user(
    data : LoginInput = Body(),
    db: Redis = Depends(get_db),
):
    token = UserController(db).login(data.username, data.password)
    return token