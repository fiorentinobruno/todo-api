from fastapi import APIRouter, Depends
from app.schemas.todo_schema import TodoCreate, TodoRead
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.services.todo_service import create_todo_sv

router = APIRouter(prefix="/todos", tags=["todos"])

@router.post("/", status_code=201, response_model=TodoRead)
async def create_todo(todo_req: TodoCreate, db: Session = Depends(get_db)):
    return create_todo_sv(db, todo_req)
