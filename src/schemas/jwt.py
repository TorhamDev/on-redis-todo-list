from pydantic import BaseModel


class JWTResponsePayload(BaseModel):
    access: str

class JWTPayload(BaseModel):
    exp: int
    username: str