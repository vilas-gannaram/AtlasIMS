from fastapi import APIRouter

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get("/")
def get_orders():
    return {"message": "Orders List"}


@router.get("/{item_id}")
def get_order(item_id: int):
    return {"item_id": item_id, "status": "checking...."}
