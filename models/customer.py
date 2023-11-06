from pydantic import BaseModel, EmailStr

class Customer(BaseModel):
    Customer_Id: int
    Nama: str
    Alamat: str
    Nomor_Hp: str
    Email: EmailStr