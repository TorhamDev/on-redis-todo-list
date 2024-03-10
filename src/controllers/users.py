from redis import Redis
from src import exceptions

class UserController:
    def __init__(self, redis_db: Redis) -> None:
        self.redis_db = redis_db
    
    def register(self, username: str, password: str):
        if self.redis_db.hgetall(f"user:{username}"):
            raise exceptions.UserAlreadyExists
        else:
            self.redis_db.hset(f"user:{username}", mapping={
                "username": username,
                "password": password
            })
