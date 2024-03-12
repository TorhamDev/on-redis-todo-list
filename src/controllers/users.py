from redis import Redis
from src import exceptions
from src.utils import PasswordHandler, JWTHandler
from src.schemas._input import UpdateUserInput


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
    
    def login(self, username: str, password: str):
        user = self.redis_db.hgetall(f"user:{username}")
        if user:
            if not PasswordHandler.verify_passowrd(user.get("password"), password):
                raise exceptions.WrongCredentials
            return JWTHandler.generate(username)
        else:
            raise exceptions.WrongCredentials

    def update_user(self, username: str, update_data: UpdateUserInput):

        if not self.redis_db.hgetall(f"user:{username}"):
            raise exceptions.UserNotFound
        
        if self.redis_db.hgetall(f"user:{update_data.new_username}"):
            raise exceptions.UsernameIsAlreadyTaken
        
        self.redis_db.rename(f"user:{username}", f"user:{update_data.new_username}")
        # maybe more updates options later

        return True