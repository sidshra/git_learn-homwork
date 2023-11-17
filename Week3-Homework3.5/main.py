#Week 3 - Homework 3.5

from dto import Author, BookItem

from fastapi import FastAPI,HTTPException
from typing import Dict, List

app = FastAPI()

my_book_items_dict : Dict[str, BookItem] = {}

@app.put("/books/{book_name}")
def create_book(book_name: str, book_item: BookItem) -> None:
    my_book_items_dict[book_name] = book_item
    print(my_book_items_dict)
    #return {"book_name" : book_name, "book_item"  : BookItem}

@app.get("/books/{book_name}") 
def get_book(book_name : str) -> BookItem:
    if book_name in my_book_items_dict.keys():   
        return my_book_items_dict[book_name]
    else:
        raise HTTPException(status_code=404, detail= "Item not found : " + book_name)
        

@app.delete("/books/{book_name}")
def delete_book(book_name : str) -> Dict:
    if book_name in my_book_items_dict.keys():
        my_book_items_dict.pop(book_name)
        print(my_book_items_dict)
        return { book_name : "Sucesssfully deleted "}      
    else:
        raise HTTPException(status_code=404, detail= "Item not found ")
        
@app.get("/books/")
def get_books() -> List[BookItem]:
    return my_book_items_dict.values()        