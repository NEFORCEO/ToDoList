from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base, mapped_column, Mapped
from sqlalchemy import String, Integer

from client.config.config import DB_URL

engine = create_async_engine(DB_URL)

session_create = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "Todo List"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, index=True) 
    task_name: Mapped[str] = mapped_column(String, index=True)
