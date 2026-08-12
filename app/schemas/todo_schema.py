from pydantic import BaseModel
import uuid

class TodoCreate(BaseModel):
    title: str
    description: str | None = None
    priority: int
    tag: str | None = None

class TodoRead(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None 
    priority: int 
    completed: bool 
    tag: str | None

class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    priority: int | None = None
    completed: bool | None = None
    tag: str | None = None