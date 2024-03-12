from fastapi import APIRouter, Body, Depends
from src.schemas._input import RegisterUserInput
from src.db._redis import get_db
from redis import Redis
from src.controllers.users import UserController
from src.utils.jwt import JWTHandler
from src.schemas.jwt import JWTPayload
from src.schemas._input import UpdateUserInput

router = APIRouter(tags=["users"])

@router.post("/register")
def register_user(
    data : RegisterUserInput = Body(),
    db: Redis = Depends(get_db)
):
    UserController(db).register(data.username, data.password)
    return data


@router.patch("/")
def update_user(
    user_info: JWTPayload = Depends(JWTHandler.verify_token),
    data: UpdateUserInput = Body(),
    db: Redis = Depends(get_db),

):
    UserController(db).update_user(username=user_info.username, update_data=data)
    
    return JWTHandler.generate(data.new_username, user_info.exp)