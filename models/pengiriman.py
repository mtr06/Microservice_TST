from pydantic import BaseModel

class Customer(BaseModel):
    Delivery_Id: int
    Transaksi_Id: int
    Nama_Kurir: str
    Nomor_Hp: str
    Estimasi_Waktu: str
    Status_Pengiriman: str