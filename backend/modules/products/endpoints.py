from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
def get_products():
    return {"message": "Products"}


@router.get("/{item_id}")
def get_product(item_id: int):
    return {"item_id": item_id, "status": "checking...."}
