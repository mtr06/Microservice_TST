from pydantic import BaseModel
import datetime

class Transaksi(BaseModel):
    Transaksi_Id: int
    Order_Id: int
    Metode: str
    IdCard: str
    Tanggal: datetime
    Total_Price: int
    Status_Pembayaran: str