from fastapi import APIRouter, Body
from src.schemas._input import RegisterUserInput
router = APIRouter(tags=["users"])

@router.post("/register")
def register_user(
    data : RegisterUserInput = Body()
):
    return data