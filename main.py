from fastapi import FastAPI
from sqlalchemy.orm import Session
from data_schemas import ProductRequest,ProductResponse

from sqlalchemy import create_engine, select,insert
from models import Base, Product, Purchase, User, Sale, Sale_detail, Payment




app = FastAPI()
# Create a database using sqlalchemy engine
engine = create_engine("sqlite:///./duka-fast-api", echo=True)

# Create tables into the database using sqlalchemy
Base.metadata.create_all(engine)

# Create a session to do sql transaction 
session = Session(engine)


@app.get("/")
def home():
    return {'Version': "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str):
#     return {"item_id": item_id, "q": q}

@app.post('/products')
def create_product(prod:ProductRequest):
    new_product=Product(
        user_id=prod.user_id,
        product_name=prod.name,
        buying_price =prod.buying_price,
        selling_price=prod.selling_price,
        stock_quantity=prod.stock_quantity
    )
    session.add(new_product)
    session.commit()
    return{'new_product':new_product}