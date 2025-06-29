from fastapi import APIRouter, Depends, HTTPException
# from pydan import

from sqlalchemy.orm import Session
from db.engine import get_db
from db.models import User, Commentss
from db import models

from pydan import user

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/", response_model=list[user.ReadUser])
async def comments(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("/", response_model=user.ReadUser)
async def comments(us: user.CreateUser, db: Session = Depends(get_db)):
    #email verification
    existing_user = db.query(User).filter(User.email == us.email).first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )
    users = User(name=us.name, email=us.email)
    db.add(users)
    db.commit()
    db.refresh(users)

    if us.comment:  # если есть комментарий, добавляем
        comment = Commentss(description=us.comment.description, user_id=users.id)
        db.add(comment)
        db.commit()
        db.refresh(users)

    return users