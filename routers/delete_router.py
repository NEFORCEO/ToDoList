
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import Todo
from database.model.models import get_session
from schemas.delete_schema.delete_schema import DeleteSchema
from schemas.return_schema import ResponseDELETESchema


delete_router = APIRouter(
    tags=["Удалить таску"],
    prefix="/delete"
)

@delete_router.delete("/delete/task/", response_model=ResponseDELETESchema)
async def delete_task(param: DeleteSchema, db: AsyncSession = Depends(get_session)):
    gang = await db.execute(select(Todo).filter(Todo.id == param.id))
    result = gang.scalar_one_or_none()
    
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Заголовка с таким айди не сущесвует"
        )
    await db.delete(result)
    await db.commit()
    return {
        "status": 200,
        "result": "Успешно"
    }