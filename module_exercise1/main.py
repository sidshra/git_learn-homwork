#Week 3 Day 1 - Homework 2

from dto import BookItem, BookStore, Author

def main():
    item_author = Author(author_name="Dan Brown",author_id="ABCD-1000")

    book_item = BookItem(book_name= "Andels & Demons",
                         author_type= item_author,
                         year_published="2023")

    book_store = BookStore(store_name="Paper Plus", 
                           book_shelve= book_item)

    my_serialized_object1 = book_store.__dict__
    print(my_serialized_object1)

if __name__ == "__main__":
    main()   