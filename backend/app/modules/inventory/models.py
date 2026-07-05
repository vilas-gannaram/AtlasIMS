import uuid

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ...core.database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)
    warehouse_id = Column(String, nullable=False)  # Simplified as string for now
    quantity_available = Column(Integer, default=0)
    quantity_reserved = Column(Integer, default=0)

    product = relationship("Product", back_populates="stock_levels")
