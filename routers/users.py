from fastapi import APIRouter, Depends, HTTPException
# from pydan import

from sqlalchemy.orm import Session
from db.engine import get_db
from db.models import User
from db import models

from pydan import user

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/", response_model=list[user.ReadUser])
async def comments(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("/", response_model=user.CreateUser)
async def comments(us: user.CreateUser, db: Session = Depends(get_db)):
    #email verification
    existing_user = db.query(User).filter(User.email == us.email).first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    users = User(name=us.name, comments=us.comments, email=us.email)
    db.add(users)
    db.commit()
    db.refresh(users)
    return users









# @router.post("/", response_model=user.CreateUser)
# async def comments(us: user.CreateUser, db: Session = Depends(get_db)):
#     #email verification
#     existing_user = db.query(User).filter(User.email == us.email).first()
#     if existing_user:
#         raise HTTPException(
#             status_code=400,
#             detail="Email already exists"
#         )
#
#     users = User(name=us.name, comments=us.comments, email=us.email)
#     db.add(users)
#     db.commit()
#     db.refresh(users)
#     return users
#
# смотри вот моя ручка на fast api для добавления user как теперь будет работать у меня ручка и вообще как работает модели типа у меня user добавляет коментарий и так же может его смотреть?
#
#
# from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
# from sqlalchemy import String, DateTime, func, ForeignKey
#
# class Base(DeclarativeBase):
#     pass
#
#
# class User(Base):
#     __tablename__ = "users"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column()
#     email: Mapped[str] = mapped_column()
#
#     comments: Mapped[list["Comment"]] = relationship(back_populates="user", cascade="all, delete")
#
#
# class Commentss(Base):
#     __tablename__ = "comments"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     description: Mapped[str] = mapped_column(String(200))
#     created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=func.now())
#
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     user: Mapped[User] = relationship(back_populates="comments")
#
# А ВОТ модели
