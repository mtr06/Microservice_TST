from pydantic import BaseModel

class Pesanan(BaseModel):
    Order_Id: int
    Customer_Id: int
    Produk_Id: int
    Jumlah: int
    Price: int