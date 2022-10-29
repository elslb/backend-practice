from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

# creating an endpoint to return the above data when the client requests it
@app.get("/store") # <-- Endpoint
def get_stores(): # <-- Function associated with above endpoint
    return {"stores": stores}


# creating an endpoint to receive data that the client sends and add it to the stored data
@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201 # Status code 201 is the default OK good


# creating an endpoint to receive dynamic paths and add items to the store
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:    # looping through stores to create items in the store matching the name from the url
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
        return {"message": "Store not found!"}, 404


# endpoint to get a specific store by name
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
        return {"message": "Store not found!"}, 404


# endpoint to get only the items from a specific store
@app.get("/store/<string:name>/item")
def get_store_item(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
        return {"message": "Store not found!"}, 404