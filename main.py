from fastapi import FastAPI
from sqlalchemy.orm import Session
from data_schemas import ProductRequest,ProductResponse,UserRequest

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

@app.post('/products', response_model=ProductResponse)
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
    return new_product

@app.post('/register')
def add_user(user:UserRequest):
    statement=select(User).where(User.email==user.email)
    is_user=session.execute(statement).first()
    if not is_user:
        new_user=User(
            full_name=user.full_name,
            email=user.email,
            password=user.password

        )
        session.add(new_user)
        session.commit()
        return{'Success':'User added succesfully'}
    else:
        return{'Error':'Error Occured'}

@app.get('/products',response_model=list[ProductResponse])
def get_products():
    query=select(Product)
    products=session.scalars(query)
    return products