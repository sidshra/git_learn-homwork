# Week 3 - Homework 3

from dto import ItemOrigin,InventoryItem
from fastapi import FastAPI,HTTPException
from typing import Dict


app = FastAPI()


my_inventory_items_dict : Dict[str, InventoryItem] = {}

@app.put("/items/{serial_number}")
def create_item(serial_number: str, invent_item: InventoryItem):
    my_inventory_items_dict[serial_number]= invent_item
    print(my_inventory_items_dict)
    #return {"serial_number" : serial_number, "invent_item" : invent_item }



@app.get("/items/{serial_number}")
def get_item(serial_number: str):
    if serial_number in my_inventory_items_dict.keys():
        return my_inventory_items_dict[serial_number]
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    

    
    


