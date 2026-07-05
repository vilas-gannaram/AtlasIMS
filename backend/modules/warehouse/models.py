import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from ...core.database import Base


class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    location_code = Column(String, unique=True, nullable=False)  # e.g., "NYC-01"
