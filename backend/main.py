from fastapi import FastAPI

from modules.inventory.endpoints import router as inventory_router
from modules.orders.endpoints import router as orders_router
from modules.products.endpoints import router as products_router
from modules.warehouse.endpoints import router as warehouse_router

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
