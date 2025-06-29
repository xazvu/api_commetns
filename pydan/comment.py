from pydantic import BaseModel

#to create a comment
class Comment(BaseModel):
    description: str


#for reading comments
class ReadComments(Comment):
    id: int
    model_config = {
        "from_attributes": True
    }
