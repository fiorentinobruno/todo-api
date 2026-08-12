from sqlalchemy.orm import Session
from app.schemas.todo_schema import TodoCreate
from app.models.todos_model import Todo

def create_todo(db: Session, todo_data: TodoCreate) -> Todo:
    new_todo = Todo(
        title=todo_data.title,
        description=todo_data.description,
        priority=todo_data.priority,
        tag=todo_data.tag
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo

