from fastapi import APIRouter, Depends
from app.db.dependencies import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text

router = APIRouter()

@router.get("/health")
def health_check(db: Session = Depends(get_db)) -> dict[str, str]:
    db.execute(text("SELECT 1"))
    return {"status": "ok"}
