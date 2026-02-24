from scalar_fastapi import get_scalar_api_reference
from fastapi import FastAPI
from app.router.todo import todo_router
from app.core.settings import settings


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)

app.include_router(todo_router, prefix="/api/v1")


@app.get("/")
def home():
    return {"message": "Welcome to Todo Apps"}


@app.get("/scalar")
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )

