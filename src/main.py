from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.routers.users import router as user_router
app = FastAPI()


@app.get("/")
def index():
    return HTMLResponse("<center><h1>Hello World!</h1></center>")

app.include_router(user_router, prefix="/users")