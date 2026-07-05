from app.core.config import settings
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

# Create the async engine
engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)

# Create a session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Base class for your models
Base = declarative_base()


# Dependency for FastAPI routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
