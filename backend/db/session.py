"""AsyncEngine (asyncpg), get_db() dependency, RLS setter."""

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from backend.config.settings import settings

engine = create_async_engine(settings.database_url, pool_size=settings.database_pool_size, echo=settings.debug)
SessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session


async def set_tenant_rls(session: AsyncSession, tenant_id: str) -> None:
    """Set Postgres RLS context for multi-tenant isolation."""
    await session.execute(f"SET app.current_tenant = '{tenant_id}'")  # noqa: S608
