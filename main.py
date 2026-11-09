from fastapi import FastAPI
from sqlalchemy.orm import Session
from data_schemas import ProductRequest,ProductResponse

from sqlalchemy import create_engine, select,insert
from models import Base, Product, Purchase, User, Sale, Sale_detail, Payment
from fastapi import FastAPI



app = FastAPI()
# Create a database using sqlalchemy engine
engine = create_engine("sqlite:///./flask_duka_api.db", echo=True)

# Create tables into the database using sqlalchemy
Base.metadata.create_all(engine)

# Create a session to do sql transaction 
session = Session(engine)


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str):
#     return {"item_id": item_id, "q": q}

@app.post('/products')
def create_product(prod:ProductRequest):
    new_product=Product(
        user_id=1,
        product_name=prod.name,
        buying_price =prod.buying_price,
        selling_price=prod.selling_price
    )
    session.add(new_product)
    return{'test':'prod'}