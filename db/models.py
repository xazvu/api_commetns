from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String

class Base(DeclarativeBase):
    pass

class Comment(Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(200))
