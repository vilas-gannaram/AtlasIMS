from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ...core.database import get_db
from .services import get_orders_list

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get("/")
async def list_orders(
    db: AsyncSession = Depends(get_db),
):
    return await get_orders_list(db)


@router.get("/{item_id}")
async def get_order(item_id: int):
    return {"item_id": item_id, "status": "checking...."}
