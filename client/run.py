from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.model.model import init_db

async def start_app(app: FastAPI):
    print("Приложение запущено")
    await init_db()
    yield
    print("Приложение завершило свою работу")