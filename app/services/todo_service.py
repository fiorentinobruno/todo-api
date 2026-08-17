from sqlalchemy.orm import Session
from app.schemas.todo_schema import TodoCreate
from app.repositories.todo_repository import create_todo
from app.models.todos_model import Todo

def create_todo_sv(db: Session, todo: TodoCreate) -> Todo:
    return create_todo(db, todo)