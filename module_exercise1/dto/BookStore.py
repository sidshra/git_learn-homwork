from pydantic import BaseModel
from .BookItem import BookItem


class BookStore(BaseModel):
    store_name : str
    book_shelve : BookItem