# Week 3 Day 1 - Homework 1

from dto import ItemOrigin,InventoryItem

def main():
    item_origin = ItemOrigin(country= "Ethiopia", production_date="22-11-98")

    my_item1 = InventoryItem(name = "Printer", 
                             quantity = 5, 
                             serial_number="ERTSDFTY",
                             origin = item_origin)
    
    my_serialize_object1 = my_item1.__dict__

    print(my_serialize_object1)
    my_item2 = InventoryItem(**my_serialize_object1)
    print(my_item2.__dict__)

if __name__ == "__main__":
    main()