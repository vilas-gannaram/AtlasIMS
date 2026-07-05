from fastapi import FastAPI

from app.modules.inventory.router import router as inventory_router
from app.modules.orders.router import router as orders_router
from app.modules.products.router import router as products_router
from app.modules.warehouse.router import router as warehouse_router

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
