from pydantic import BaseModel
class ProductRequest(BaseModel):
    name : str
    buying_price : float
    selling_price:float
    stock_quantity:int

class ProductResponse(BaseModel):
    id : int 
    name : str
    buying_price:float
    selling_price:float
    stock_quantity:int