from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Order, OrderItem


async def get_orders_list(db: AsyncSession):
    result = await db.execute(select(Order))
    return result.scalars().all()


# async def get_inventory_item(item_id: UUID, db: AsyncSession) -> Inventory | None:
#     result = await db.execute(select(Inventory).where(Inventory.id == item_id))
#     return result.scalar_one_or_none()
