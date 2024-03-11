from pydantic import BaseModel


class JWTPayload(BaseModel):
    access: str