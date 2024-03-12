import jwt
from datetime import datetime, timedelta
from src.settings import get_settings
from fastapi.exceptions import HTTPException
from fastapi import status, Header
from src.schemas.jwt import JWTResponsePayload, JWTPayload
from typing import Annotated


settings = get_settings()

class JWTHandler:
    def generate(username: str) -> JWTResponsePayload:
        expire_time = settings.ACCESS_TOKEN_EXPIRE_MINUTES

        secret_key = settings.SECRET_KEY

        expires_delta = datetime.utcnow() + timedelta(minutes=expire_time)

        to_encode = {"exp": expires_delta, "username": username}
        encoded_jwt = jwt.encode(to_encode, secret_key, settings.ALGORITHM)

        return JWTResponsePayload(access=encoded_jwt)
    
    def verify_token(auth_token: Annotated[str, Header()]) -> dict:
        jwt_token = auth_token
        if not jwt_token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="auth header not found.",               
            )
        try:
            token_data = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

            if datetime.fromtimestamp(token_data["exp"]) < datetime.now():
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token expired",
                    headers={"WWW-Authenticate": "Bearer"},
                )
        except jwt.exceptions.PyJWTError:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return JWTPayload(**token_data)    
