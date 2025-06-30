from pydantic import BaseModel, EmailStr
from typing import Optional


class CreateUser(BaseModel):
    name: str
    email: EmailStr
    comment: str


class ReadUser(CreateUser):
    id: int

    model_config = {
        "from_attributes": True
    }
