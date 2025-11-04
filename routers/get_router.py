from fastapi import APIRouter, Depends, Response, HTTPException

from database.db import Todo
from database.model.models import AsyncSession, get_session
from sqlalchemy import select

from schemas.create_task.create_task import CreateTask
from schemas.delete_schema.delete_schema import DeleteSchema
from schemas.patch_schema.patch_schema import PatchSchema
from schemas.return_schema import ResponseDELETESchema, ResponseGetSchema, ResponsePOSTSchema, ResponsePATCHSchema

get_router = APIRouter(
    tags=["Посмотреть все таски"],
    prefix="/todo"
)

@get_router.get("/read", response_model=ResponseGetSchema)
async def read_task(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Todo))
    get_todo_all = result.scalars().all()
    return {
        "status": 200,
        "result": get_todo_all
    }

    
    
    