import pyodbc
server = 'sql18221064.database.windows.net' 
database = 'DeliveryDatabase' 
username = 'admin_18221064' 
password = 'Lostsaga098!' 
coonection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:sql18221064.database.windows.net,1433;Database=DeliveryDatabase;Uid=admin_18221064;Pwd=Lostsaga098!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
cnxn = pyodbc.connect(coonection_string)

from fastapi import	APIRouter,	Body,	HTTPException,	status	
from models.customer import Customer	
from models.pesanan import Pesanan	

customer_router =	APIRouter(	
tags=["Customers"]	
)

@customer_router.get("/{cus_id}")
async def get_profile(cus_id: int):	
    customer = []
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM Customer")

    for row in cursor.fetchall():
        if (row.Customer_Id == cus_id):
            customer.append(f"{row.Nama}, {row.Alamat}, {row.Nomor_Hp}, {row.Email}")
            return customer
    raise	HTTPException(	status_code=status.	HTTP_404_NOT_FOUND,	detail="Customer Tidak Ditemukan!"	)

@customer_router.post("/create_customer")
async	def	create_customer(data: Customer):	
    customers = []
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM Customer")
    last_id = 0
    for row in cursor.fetchall():
        customers.append(f"{row.Customer_Id}, {row.Nama}, {row.Alamat}, {row.Nomor_Hp}, {row.Email}")
        last_id+=1

    if data.Email in customers[4]:
        raise	HTTPException(status_code=status.HTTP_409_CONFLICT,	detail="Email Sudah Ada!")
    else:
        cursor.execute(f"INSERT INTO Customer (Customer_Id, Nama, Alamat, Nomor_Hp, Email) VALUES (?, ?, ?, ?, ?)", last_id+1, data.Nama, data.Alamat, data.Nomor_Hp, data.Email)
        cnxn.commit()
        return {"message":	"Customer Berhasil Dibuat!"}	
    
@customer_router.post("/{cus_id}/create_order")
async def create_order(order: Pesanan):
    cursor = cnxn.cursor()
    try:
        cursor.execute("INSERT INTO Pesanan (Order_Id, Customer_Id, Produk_Id, Jumlah, Price) VALUES (?, ?, ?, ?, ?)",
                       (order.Order_Id, order.Customer_Id, order.Produk_Id, order.Jumlah, order.Price))
        cnxn.commit()
        return {"message": "Pengiriman berhasil dibuat"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Gagal membuat pesanan!")
    
@customer_router.get("/{cus_id}/pembayaran")
async def get_transaksi(cus_id: int):
    transaksi = []
    cursor = cnxn.cursor()
    cursor.execute("Select DISTINCT transaksi.Order_Id, Metode, IdCard, Tanggal, Total_Price, Status_Pembayaran from transaksi INNER JOIN pesanan ON transaksi.Order_Id = pesanan.Order_Id WHERE Customer_Id = ?", cus_id)
    for row in cursor.fetchall():
        transaksi.append(f"{row.Order_Id}, {row.Metode}, {row.IdCard}, {row.Tanggal}, {row.Total_Price}, {row.Status_Pembayaran}")
    if(len(transaksi) != 0):
        return transaksi
    else:
        raise	HTTPException(	status_code=status.	HTTP_404_NOT_FOUND,	detail="Transaksi Tidak Ditemukan!"	)


@customer_router.get("/{cus_id}/pengiriman")
async def get_pengiriman(cus_id: int):
    pengriman = []
    cursor = cnxn.cursor()
    cursor.execute("Select DISTINCT Transaksi_Id, transaksi.Order_Id, Metode, IdCard, Tanggal, Total_Price, Status_Pembayaran from transaksi INNER JOIN pesanan ON transaksi.Order_Id = pesanan.Order_Id WHERE Customer_Id = ?", cus_id)
    for row in cursor.fetchall():
        transaksi_id = f"{row.Transaksi_Id}"
    cursor.execute("Select DISTINCT Delivery_Id, Nama_Kurir, Nomor_Hp, Estimasi_Waktu, Status_Pengiriman from pengiriman WHERE Transaksi_Id = ?", transaksi_id)
    print(transaksi_id)
    for row in cursor.fetchall():
        pengriman.append(f"{row.Delivery_Id}, {row.Nama_Kurir}, {row.Nomor_Hp}, {row.Estimasi_Waktu}, {row.Status_Pengiriman}")
    if(len(pengriman) != 0):
        return pengriman
    else:
        raise	HTTPException(	status_code=status.	HTTP_404_NOT_FOUND,	detail="Pengiriman Tidak Ditemukan!"	)