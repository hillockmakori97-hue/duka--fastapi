from pydantic import BaseModel
class ProductRequest(BaseModel):
    name : str
    user_id: int
    buying_price : float
    selling_price:float
    stock_quantity:int

class ProductResponse(BaseModel):
    id : int 
    user_id: int
    name : str
    buying_price:float
    selling_price:float
    stock_quantity:int


class UserRequest(BaseModel):
    full_name:str
    email:str
    password:str
