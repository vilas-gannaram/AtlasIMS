from fastapi import APIRouter

router = APIRouter(prefix="/inventory", tags=["inventory"])


@router.get("/")
def get_inventory():
    return {"message": "Inventory List"}


@router.get("/{item_id}")
def get_inventory_item(item_id: int):
    return {"item_id": item_id, "status": "in_stock"}
