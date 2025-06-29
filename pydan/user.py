from pydantic import BaseModel, EmailStr
from typing import Optional

from .comment import ReadComments
from .comment import CreateComment

class CreateUser(BaseModel):
    name: str
    email: EmailStr
    comment: Optional[CreateComment] = None  # список комментариев, а не строка


class ReadUser(BaseModel):
    id: int
    name: str
    email: EmailStr
    comments: list[ReadComments] = []

    model_config = {
        "from_attributes": True
    }
