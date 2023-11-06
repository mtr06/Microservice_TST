# Microservice_TST

### Order Delivery ###

API ini digunakan untuk melihat produk, memesan produk, melihat pembayaran, serta pengiriman

Command:
- get("/produk/") --> melihat semua produk yang ada
- post("/create_customer") --> membuat customer baru
- get("/{cus_id}") --> melihat profile customer
- post("/{cust_id}/create_order") --> membuat pesanan
- get("/{cust_id}/pembayaran") --> melihat pembayaran
- get("/{cust_id}/pengiriman") --> melihat pengiriman

### Requirement ###

1. Python 3
2. Ms OBCD Driver SQL (untuk terhubung ke database azure)
