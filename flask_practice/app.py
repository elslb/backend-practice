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