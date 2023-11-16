from pydantic import BaseModel, field_validator
from .Author import Author

class BookItem(BaseModel):
    book_name : str
    author_type : Author 
    year_published : int

    @field_validator("year_published") #
    @classmethod

    def check_valid_year(cls, year_published : int):        #cls refers to class itself
        assert year_published > 2022 and year_published < 3000 , "Year published should be between the range : 2023 - 3000"
        return year_published

 