from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.routes import todo_router

from app.db.dependencies import get_db

app = FastAPI(title="Todo API")

app.include_router(todo_router.router)