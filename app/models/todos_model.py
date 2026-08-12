import uuid
from sqlalchemy import Uuid
from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(nullable=True)
    priority: Mapped[int] = mapped_column(nullable=False)
    completed: Mapped[bool] = mapped_column(nullable=False, default=False)
    tag: Mapped[str | None] = mapped_column(nullable=True)

