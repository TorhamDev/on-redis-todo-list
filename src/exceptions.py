from fastapi.exceptions import HTTPException
from fastapi import status


class BaseException(HTTPException):
    status_code = 400
    detail = "Bad request"

    def __init__(self) -> None:
        self.status_code = self.status_code
        self.detail = self.detail


class UserAlreadyExists(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "User already exists."


class WrongCredentials(BaseException):
    status_code = 403
    detail = "wrong credentials."