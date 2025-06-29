from pydantic import BaseModel

#to create a comment
class CreateComment(BaseModel):
    description: str


#for reading comments
class ReadComments(CreateComment):
    id: int

    model_config = {
        "from_attributes": True
    }


