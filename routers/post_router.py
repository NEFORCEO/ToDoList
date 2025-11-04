
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import Todo
from database.model.models import get_session
from schemas.create_task.create_task import CreateTask
from schemas.return_schema import ResponsePOSTSchema


post_router = APIRouter(
    tags=["Добавить таску"]
)

@post_router.post("/create/task", response_model=ResponsePOSTSchema)
async def create_task(param: CreateTask, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Todo).filter(Todo.title == param.title))
    existing_task = result.scalar_one_or_none()
    
    if existing_task:
        raise HTTPException(
            status_code=409,
            detail="Такой заголовок уже существует"
        )
        
    new_task = Todo(title=param.title, task_name=param.task_name)
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return {
        "status": 200,
        "id": new_task.id,
        "title": new_task.title,
        "task_name": new_task.task_name
    }