from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    name: str
    comments: str
    email: EmailStr


class ReadUser(CreateUser):
    id: int

    model_config = {
        "from_attributes": True
    }