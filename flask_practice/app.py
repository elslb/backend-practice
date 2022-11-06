from flask import Flask, request
from db import items, stores
import uuid

app = Flask(__name__)

# creating an endpoint to return the above data when the client requests it
@app.get("/store") # <-- Endpoint
def get_stores(): # <-- Function associated with above endpoint
    return {"stores": list(stores.values())}
    # ^ needs to be cast into a list because stores.values behaves like a list but is not actually one
    # this is in order for it to be turned into JSON


# creating an endpoint to receive data that the client sends and add it to the stored data
@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex # will not need to do this when using an actual DB
    store = {**store_data, "id": store_id} # **store_data passes that kwarg into this new dict and unpacks the values in it
    stores[store_id] = store
    return store, 201 # Status code 201 is the default OK good


# creating an endpoint to receive dynamic paths and add items to the store
@app.post("/store/<string:name>/item")
def create_item(name): # name comes from the url portion 'string:name'
    request_data = request.get_json()
    for store in stores:    # looping through stores to create items in the store matching the name from the url
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
        return {"message": "Store not found!"}, 404


# endpoint to get a specific store by name
@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message": "Store not found!"}, 404


# endpoint to get only the items from a specific store by name
@app.get("/store/<string:name>/item")
def get_store_item(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
        return {"message": "Store not found!"}, 404