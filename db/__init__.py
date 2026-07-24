from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os

DB_URL = os.getenv("DB_URL")

engine = create_async_engine(url="postgresql+asyncpg://maxim_user:f70Zs6w8y94UQFhf@217.107.34.79:49159/maxim_db", echo=False)
session_factory = async_sessionmaker(engine)

