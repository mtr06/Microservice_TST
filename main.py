from	fastapi import	FastAPI
from	routes.produk import	produk_router
from	routes.customer import	customer_router
# from	routes.pesanan import	pesanan_router
import	uvicorn
app	=	FastAPI()	#	Register	routes	

app.include_router(produk_router,	prefix="/produk")
# app.include_router(pesanan_router,	prefix="/pesan")	
app.include_router(customer_router,	prefix="")		

if	__name__	==	"__main__":
    uvicorn.run("main:app",	host="0.0.0.0",	port=8000,	reload=True)