from fastapi import APIRouter

router = APIRouter(prefix="/warehouse", tags=["Warehouse"])


@router.get("/")
def get_warehouses():
    return {"message": "List of warehouses"}


@router.get("/{item_id}")
def get_warehouse(item_id: int):
    return {"warehouse_id": item_id, "status": "checking...."}
