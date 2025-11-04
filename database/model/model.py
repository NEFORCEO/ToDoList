from typing import Annotated

from fastapi import Depends

from database.db import engine, Base, AsyncSession, session_create

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
async def get_session() -> AsyncSession:
    async with session_create() as session:
        yield session
    
SessionDep = Annotated[AsyncSession, Depends(get_session)]
    