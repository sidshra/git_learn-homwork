from pydantic import BaseModel

class Author(BaseModel):
    author_name : str
    author_id : str

