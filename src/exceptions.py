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


class UserNotFound(BaseException):
    status_code = 404
    detail = "User not found."

class UsernameIsAlreadyTaken(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "This username is already taken."