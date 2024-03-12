from redis import Redis
from src.schemas._input import CreateTodoInput
from src.schemas.output import TodoDetailsOutput
from uuid import uuid4


class TodoController:
    def __init__(self, redis_db: Redis) -> None:
        self.redis_db = redis_db
    
    def create_todo(self, username: str, todo_data: CreateTodoInput) -> TodoDetailsOutput:
        
        task_id = str(uuid4())
        task_data = {
            "id":task_id,
            "title":todo_data.title,
            "details": todo_data.details
        }
        self.redis_db.lpush(f"user:{username}:todos", task_id, todo_data.title)
        self.redis_db.hset(f"user:{username}:todo:{task_id}", mapping=task_data)

        return TodoDetailsOutput(**task_data)
