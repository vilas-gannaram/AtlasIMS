from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ...core.database import get_db
from .services import get_inventory_item, get_inventory_list

router = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.get("/")
async def list_inventory(
    db: AsyncSession = Depends(get_db),
):
    return await get_inventory_list(db)


@router.get("/{item_id}")
async def get_inventory(
    item_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await get_inventory_item(item_id, db)
