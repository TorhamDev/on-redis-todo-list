from fastapi import APIRouter

router = APIRouter(tags=["todo"])

@router.post("/")
def create_todo():
    ...

@router.get("/")
def get_all_todos():
    ...

@router.get("/{todo_id}/")
def get_a_todo():
    ...

@router.put("/{todo_id}")
def update_a_todo():
    ...