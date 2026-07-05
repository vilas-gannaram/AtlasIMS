from fastapi import FastAPI

from modules.inventory.router import router as inventory_router
from modules.orders.router import router as orders_router
from modules.products.router import router as products_router
from modules.warehouse.router import router as warehouse_router

app = FastAPI()

app.include_router(inventory_router)
app.include_router(orders_router)
app.include_router(products_router)
app.include_router(warehouse_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def check_health():
    return {"Health": "Ok"}
