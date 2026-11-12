from fastapi import FastAPI,HTTPException
from sqlalchemy.orm import Session
from data_schemas import ProductRequest,ProductResponse,UserRequest,PurchaseRequest,PurchaseResponse,SalesRequest,SaleDetailRequest,SalesResponse,SaleDetailResponse,PaymentRequest,PaymentResponse

from sqlalchemy import create_engine, select,insert
from models import Base, Product, Purchase, User, Sale, Sale_detail, Payment
from datetime import datetime,date



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


# def add_user():
#     # statement=select(User).where(User.email==user.email)
#     # is_user=session.execute(statement).first()
    
#     new_user=User(
#         full_name='hillock',
#         email='hillockmakori97@gmail.com',
#         password='rs3040bt'

#     )
#     session.add(new_user)
#     session.commit()
#     return{'Success':'User added succesfully'}
# add_user()

# products route

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


@app.get('/products',response_model=list[ProductResponse])
def get_products():
    query=select(Product)
    products=session.scalars(query)
    return products

@app.put('/products/{product_id}',response_model=ProductResponse)
def update_product(product_id : int,prod:ProductRequest):
    query = select(Product).where(Product.id == product_id)
    product=session.scalars(query).first()

    if product is None:
        raise HTTPException(
            status_code=404,detail='product not found'
        )

    product.product_name=prod.name
    product.buying_price=prod.buying_price
    product.selling_price=prod.selling_price
    product.stock_quantity=prod.stock_quantity
    session.commit()
    return product

@app.get("/products/{product_id}", response_model=ProductResponse)
def get_single_product(product_id):
    query = select(Product).where(Product.id == product_id)
    product = session.scalars(query).first()
    
    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return product

# end of products route 




# --------------------- Purchase routes
@app.get('/purchases',response_model=list[PurchaseResponse])
def get_purchases():
    query=select(Purchase)
    purchases=session.scalars(query)
    return purchases



@app.post('/purchases',response_model=PurchaseResponse)
def post_purchases(prse:PurchaseRequest):
    new_purchase=Purchase(
        product_id=prse.product_id,
        purchase_price=prse.purchase_price,
        date_purchased=datetime.now().date()
        
    )
    session.add(new_purchase)
    session.commit()
    return new_purchase

# ---------------end of purchases------------


# -----------------sale routes ----------

@app.get('/sales',response_model=list[SalesResponse])
def get_sales():
    query=select(Sale)
    sales=session.scalars(query)
    return sales


@app.post('/sales',response_model=SalesResponse)
def post_sales(sale:SalesRequest):
    new_sale=Sale(
        user_id=sale.user_id,
        product_id=sale.product_id,
        date_sold=datetime.now().date(),
        # product=sale.product,
        # payment=sale.payment
    )
    session.add(new_sale)
    session.commit()
    return new_sale

# ================== end of sale routes =========================

# ========================sale detail routes ==================


@app.get('/sale-details', response_model=list[SaleDetailResponse])
def get_sale_details():
    query = select(Sale_detail)
    sale_details = session.scalars(query).all()
    return sale_details

@app.post('/sale-details', response_model=SaleDetailResponse)
def post_sale_detail(detail: SaleDetailRequest):
    new_detail = Sale_detail(
        product_id=detail.product_id,
        sale_id=detail.sale_id,
        quantity=detail.quantity,
        amount=detail.amount
    )
    session.add(new_detail)
    session.commit()
    session.refresh(new_detail)
    return new_detail

# =============================end of sale detail routes ========================



@app.post("/payments", response_model=PaymentResponse)
def create_payment(payment: PaymentRequest):
    dbpayment = Payment(
        sale_id=payment.sale_id,
        amount=payment.amount,
        transaction_code=payment.transaction_code,
        mrid=payment.mrid,
        crid=payment.crid,
        status=payment.payment_status,
        phone_number=payment.phone_number
    )
    session.add(dbpayment)
    session.commit()
    return dbpayment


