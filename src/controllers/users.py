from redis import Redis
from src import exceptions
from src.utils import PasswordHandler


class UserController:
    def __init__(self, redis_db: Redis) -> None:
        self.redis_db = redis_db
    
    def register(self, username: str, password: str):
        if self.redis_db.hgetall(f"user:{username}"):
            raise exceptions.UserAlreadyExists
        else:
            hashed_pass = PasswordHandler.hash_pass(password)
            self.redis_db.hset(f"user:{username}", mapping={
                "username": username,
                "password": hashed_pass
            })
