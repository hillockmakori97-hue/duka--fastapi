from pydantic import BaseModel,ConfigDict
from datetime import date
from typing import Optional
class ProductRequest(BaseModel):
    name : str
    user_id: int
    buying_price : float
    selling_price:float
    stock_quantity:int

class ProductResponse(BaseModel):
    id:int
    user_id: int
    product_name : str
    buying_price:float
    selling_price:float
    stock_quantity:int


class UserRequest(BaseModel):
    full_name:str
    email:str
    password:str


class SalesRequest(BaseModel):
    user_id:int
    product_id:int
    date_sold: date
    product: int
    payment:float

class SalesResponse(BaseModel):
    id:int
    user_id:int
    product_id:int
    date_sold:date
    product: Optional[str] = None
    payment: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)


class PurchaseRequest(BaseModel):
    product_id:int
    purchase_price:int
    date_purchased:int 


class PurchaseResponse(BaseModel):
    id:int
    product_id:int 
    purchase_price:int 
    date_purchased:date


class PaymentRequest(BaseModel):
    sale_id:int
    # date_paid:Mapped[date]=mapped_column(Date)
    amount:float
    transaction_code:str
    mrid:str
    crid:str
    status:str
    phone_number:int
    sale:int


class PaymentResponse(BaseModel):
    id:int
    sale_id:int
    # date_paid:Mapped[date]=mapped_column(Date)
    amount:float
    transaction_code:str
    mrid:str
    crid:str
    status:str
    phone_number:str
    sale:int



class SaleDetailRequest(BaseModel):
    product_id: int
    sale_id: int
    quantity: float
    amount: int

class SaleDetailResponse(BaseModel):
    id: int
    product_id: int
    sale_id: int
    quantity: float
    amount: int

class PaymentRequest(BaseModel):
    sale_id : int
    amount : float
    transaction_code : str 
    mrid : str
    crid : str
    payment_status : str 
    phone_number : str

class PaymentResponse(BaseModel):
    id : int
    sale_id : int
    amount : float
    transaction_code : str 
    mrid : str
    crid : str
    status : str
    phone_number : str