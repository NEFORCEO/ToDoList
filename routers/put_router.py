

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import Todo
from database.model.models import get_session
from schemas.patch_schema.patch_schema import PatchSchema
from schemas.return_schema import ResponsePATCHSchema


put_router = APIRouter(
    tags=["Обновить таску"],
    prefix="/put"
)

@put_router.patch("/patch/task/{id}", response_model=ResponsePATCHSchema)
async def patch_task(id: int, param: PatchSchema, db: AsyncSession = Depends(get_session)):
    gang = await db.execute(select(Todo).filter(Todo.id == id))
    result = gang.scalar_one_or_none() 
    
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Залоговка с таким айди не сущесвует"
        )
    
    if param.title is not None:
        result.title = param.title
        
    await db.commit()
    return {
        "status": 200,
        "title": result.title
    }
    