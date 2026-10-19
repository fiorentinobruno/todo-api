from sqlalchemy.orm import Session
from app.schemas.todo_schema import TodoCreate, TodoRead, TodoUpdate
from app.repositories import todo_repository
from app.models.todos_model import Todo

def create_todo_sv(db: Session, todo: TodoCreate) -> Todo:
    return todo_repository.create_todo(db, todo)

def read_all_todos_sv(db: Session) -> list[Todo]:
    return todo_repository.read_all_todos(db)
