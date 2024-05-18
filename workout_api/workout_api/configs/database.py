from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+asyncpg://postgres:643122@localhost/dbname"

engine = create_async_engine(
    DATABASE_URL ,
    echo=True,
    pool_size=20
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

Base = declarative_base()

async def get_session():
    async with SessionLocal() as session:
        yield session