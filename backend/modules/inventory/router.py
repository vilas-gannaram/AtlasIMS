from fastapi import APIRouter

from .services import get_inventory_item, get_inventory_list

router = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.get("/")
def get_inventory():
    return get_inventory_list()


@router.get("/{item_id}")
def get_inventory_by_id(item_id):
    return get_inventory_item(item_id)
