import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USER = os.getenv("DB_USER")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


DB_ENGINE = create_async_engine(DB_URL, future=True)
async_session = async_sessionmaker(DB_ENGINE, expire_on_commit=False)
