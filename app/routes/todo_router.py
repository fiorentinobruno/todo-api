from fastapi import APIRouter, Depends
from app.schemas.todo_schema import TodoCreate, TodoRead
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.services import todo_service

router = APIRouter(prefix="/todos", tags=["todos"])

@router.post("/", status_code=201, response_model=TodoRead)
def create_todo(todo_req: TodoCreate, db: Session = Depends(get_db)):
    return todo_service.create_todo_sv(db, todo_req)

@router.get("/", response_model=list[TodoRead])
def read_all_todos(db: Session = Depends(get_db)):
    return todo_service.read_all_todos_sv(db)