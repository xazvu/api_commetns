from fastapi import APIRouter, Depends
from pydan import comment

from sqlalchemy.orm import Session
from db.engine import get_db
from db.models import Commentss


router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)

@router.get("/", response_model=list[comment.ReadComments])
async def comments(db: Session = Depends(get_db)):
    return db.query(Commentss).all()

