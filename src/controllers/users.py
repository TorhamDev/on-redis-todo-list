from redis import Redis

class UserController:
    def __init__(self, redis_db: Redis) -> None:
        self.redis_db = redis_db
    
    def register(self, username: str, password: str):
        if not self.redis_db.hgetall(f"user:{username}"):
            self.redis_db.hset(f"user:{username}", mapping={
                "username": username,
                "password": password
            })
        else:
            raise ... # TODO