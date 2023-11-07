import pyodbc
server = 'sql18221064.database.windows.net' 
database = 'DeliveryDatabase' 
username = 'admin_18221064' 
password = 'Lostsaga098!' 
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:sql18221064.database.windows.net,1433;Database=DeliveryDatabase;Uid=admin_18221064;Pwd=Lostsaga098!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
cnxn = pyodbc.connect(connection_string)

from fastapi import	APIRouter,	Body,	HTTPException,	status	
from models.produk import Produk	

produk_router =	APIRouter(	
tags=["Produks"]	
)

@produk_router.get("/")
async def retrieve_all_produks():	
    produks = []
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM Produk")

    for row in cursor.fetchall():
        print(row.Produk_Id, row.Nama, row.Harga, row.Gambar)
        produks.append(f"{row.Produk_Id}, {row.Nama}, {row.Harga}, {row.Gambar}")
    return produks


@produk_router.get("/")
async def retrieve_all_produks():	
    produks = []
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM Produk")

    for row in cursor.fetchall():
        print(row.Produk_Id, row.Nama, row.Harga, row.Gambar)
        produks.append(f"{row.Produk_Id}, {row.Nama}, {row.Harga}, {row.Gambar}")
    return produks