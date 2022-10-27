from flask import Flask

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