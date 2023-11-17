from pydantic import BaseModel, field_validator
import re

class Author(BaseModel):
    author_name : str
    author_id : str

    @field_validator("author_name")    #Validate for Author name to begin with Capital letter
    @classmethod

    def check_valid_name(cls, author_name: str):
               
        assert author_name[0].isupper() == True, "The Author name should start with capital case"
            
        return  author_name
    
    """Validate for Author id to have 9 characters 
    & in the format XXXX-YYYY
    with X being alphabets & Y being integers
    """
    
    @field_validator("author_id")   
    @classmethod

    def check_valid_id(cls, author_id : str):        #cls refers to class itself
        chk_id = re.search(r"[A-Z]{4}-[0-9]{4}",author_id)
        assert chk_id != None and len(author_id) == 9,  "The format of author_id XXXX-YYYY should have 9 characters with XXXX being capital alphabets & YYYY being numbers"
        #print(len(author_id))
        return author_id       

