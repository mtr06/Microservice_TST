from pydantic import BaseModel

class Produk(BaseModel):
    Produk_Id: int
    Nama: str
    Harga: int
    Gambar: str