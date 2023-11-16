#Week 3 Day 1 - Homework 2

from dto import BookItem, BookStore, Author

def main():
    # First object
    item_author = Author(author_name="Dan Brown",author_id="ABCD-1000")

    book_item = BookItem(book_name= "Angels & Demons",
                         author_type= item_author,
                         year_published="2023")

    book_store = BookStore(store_name="Paper Plus", 
                           book_shelve= book_item)

    my_serialized_object1 = book_store.__dict__
    print(my_serialized_object1)

    #Second object
    item_author = Author(author_name="Lee Child",author_id="ABCD-2000")

    book_item = BookItem(book_name= "One Shot",
                         author_type= item_author,
                         year_published="2024")

    book_store = BookStore(store_name="Whitcoulls", 
                           book_shelve= book_item)

    my_serialized_object2 = book_store.__dict__
    print(my_serialized_object2)

if __name__ == "__main__":
    main()   