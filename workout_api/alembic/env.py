from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from alembic import context
from workout_api.configs.database import Base  # substitua pelo caminho correto para os seus modelos

DATABASE_URL = "postgresql+asyncpg://workout:workout@localhost/workout"

def run_migrations_online():
    connectable: AsyncEngine = create_async_engine(DATABASE_URL, poolclass=pool.NullPool)
    
    async def do_run_migrations(connection):
        context.configure(connection=connection, target_metadata=Base.metadata)
        
        with context.begin_transaction():
            context.run_migrations()

    async def async_main():
        async with connectable.connect() as connection:
            await connection.run_sync(do_run_migrations)

    import asyncio
    asyncio.run(async_main())

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
