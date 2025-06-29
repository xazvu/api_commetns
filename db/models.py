from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String

class Base(DeclarativeBase):
    pass

class Commentss(Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(200))


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    comments: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column()