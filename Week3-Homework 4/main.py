# Week 3 - Homework 3

from dto import ItemOrigin,InventoryItem
from fastapi import FastAPI,HTTPException
from typing import Dict, List


app = FastAPI()


my_inventory_items_dict : Dict[str, InventoryItem] = {}

@app.put("/items/{serial_number}") 
def create_item(serial_number: str, invent_item: InventoryItem) -> None:
    my_inventory_items_dict[serial_number]= invent_item
    print(my_inventory_items_dict)
    #return {"serial_number" : serial_number, "invent_item" : invent_item }



@app.get("/items/{serial_number}")
def get_item(serial_number: str) -> InventoryItem:
    if serial_number in my_inventory_items_dict.keys():
        return my_inventory_items_dict[serial_number]
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
@app.delete("/items/{serial_number}")  
def delete_item(serial_number: str) -> Dict:  
    if serial_number in my_inventory_items_dict.keys():
        my_inventory_items_dict.pop(serial_number)
        print(my_inventory_items_dict)
        return {"msg": "Successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
    
@app.get("/items/")
def get_items() -> List[InventoryItem]:
    
    return my_inventory_items_dict.values()
  

