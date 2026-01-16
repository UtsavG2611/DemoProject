from fastapi import FastAPI
from data import Product
from database import getData
from database import add_data, update_data, delete_data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins = ["http://localhost:3000"],
                   allow_methods = ['*']

)

listOfProducts = [
    Product(
        id=1,
        name="laptop",
        description="Dell Laptop",
        price=150,
        quantity=10
    ),
    Product(
        id=2,
        name="laptop",
        description="Apple Laptop",
        price=250,
        quantity=15
    ),
    Product(
        id=3,
        name="phone",
        description="Apple phone",
        price=250,
        quantity=15
    ),
    Product(
        id=4,
        name="phone",
        description="Samsung phone",
        price=250,
        quantity=15
    )
]

@app.get("/products/")
def get_products_from_db():
    return getData()

@app.get("/Productss/{id}")
def get_product_by_id(id: int):
    products = getData()
    for p in products:
        if p.id == id:
            return p
    return {"error": "Product not found"}

from database import add_data
from data import Product

@app.post("/products/")
def add_product(product: Product):
    return add_data(product)

@app.put("/products/{id}")
def update_product(id: int, product: Product):
    return update_data(id, product)

@app.delete("/products/{id}")
def delete_product(id: int):
    return delete_data(id)