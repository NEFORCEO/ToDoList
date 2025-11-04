from fastapi import APIRouter, Depends

from database.db import Todo
from database.model.models import AsyncSession, get_session
from sqlalchemy import select

from schemas.return_schema import ResponseSchema

router = APIRouter(
    tags=["CRUD"],
    prefix="/todo"
)

@router.get("/read", response_model=ResponseSchema)
async def read_task(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Todo))
    get_todo_all = result.scalars().all()
    return {
        "status": 200,
        "result": get_todo_all
    }
