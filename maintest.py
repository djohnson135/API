from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


from Database import test #Only import the function directly into current namespace
# test() #prints "Hello"
# print (myvar)     #Exception (NameError)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None
    

app = FastAPI()

#GET
#POST
#PUT/ PATCH
#DELETE

#run server with uvicorn main:app --reload


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
def insert_item(item: Item):
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "is_offer": item.is_offer}