from redis import Redis
from src.schemas._input import TodoInput
from src.schemas.output import TodoDetailsOutput, TodoListDetailsOutput, TodoSimpleOutput
from uuid import uuid4
from src.utils.generics import divide_chunks
from src import exceptions


class TodoController:
    def __init__(self, redis_db: Redis) -> None:
        self.redis_db = redis_db
    
    def create(self, username: str, todo_data: TodoInput) -> TodoDetailsOutput:
        
        task_id = str(uuid4())
        task_data = {
            "id":task_id,
            "title":todo_data.title,
            "details": todo_data.details
        }
        self.redis_db.lpush(f"user:{username}:todos", task_id, todo_data.title)
        self.redis_db.hset(f"user:{username}:todo:{task_id}", mapping=task_data)

        return TodoDetailsOutput(**task_data)
    
    def get_all(self, username: str) -> TodoListDetailsOutput:
        
        all_todos = tuple(divide_chunks(self.redis_db.lrange(f"user:{username}:todos", 0, -1), 2))
        
        data = [TodoSimpleOutput(id=todo[1], title=todo[0]) for todo in all_todos]
        
        return TodoListDetailsOutput(todos=data)
    
    def get_one(self, username: str, todo_id: str) -> TodoDetailsOutput:

        todo = self.redis_db.hgetall(f"user:{username}:todo:{todo_id}")
        
        if not todo:
            raise exceptions.NotFound
        
        return TodoDetailsOutput(**todo)
    
    def update(self, username: str, todo_id: str, data: TodoInput) -> TodoDetailsOutput:


        todos = self.redis_db.lrange(f"user:{username}:todos", 0, -1)
        todo_data = self.redis_db.hgetall(f"user:{username}:todo:{todo_id}")
        index_to_update = None
        for t_index in range(1, len(todos), 2):
            if todo_id == todos[t_index]:
                index_to_update = t_index - 1
        
        if index_to_update is None:
            raise exceptions.NotFound
        
        to_update = {
                "id":todo_data["id"],
                "title":data.title if data.title else todo_data["title"],
                "details":data.details if data.details else todo_data["details"]
            }
        # update title in titles list
        self.redis_db.lset(f"user:{username}:todos", index_to_update, to_update["title"])

        # update the hash of todo data
        self.redis_db.hset(
            f"user:{username}:todo:{todo_id}",
            mapping=to_update
        )

        return TodoDetailsOutput(**to_update)
    

    def delete(self, username:str, todo_id: str) -> None:

        todos = self.redis_db.lrange(f"user:{username}:todos", 0, -1)
        id_to_del = None
        title_to_del = None
        for t_index in range(1, len(todos), 2):
            if todo_id == todos[t_index]:
                id_to_del = t_index
                title_to_del = t_index - 1
        

        self.redis_db.lset(f"user:{username}:todos", id_to_del, "TO_BE_DELETED")
        self.redis_db.lset(f"user:{username}:todos", title_to_del, "TO_BE_DELETED")
        self.redis_db.lrem(f"user:{username}:todos", 2, value="TO_BE_DELETED")

        self.redis_db.delete(f"user:{username}:todo:{todo_id}")