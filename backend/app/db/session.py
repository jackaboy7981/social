# session.py
# Shared async engine used by data_provider layers for raw SQL queries.
import os

from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = os.environ.get(
    "DATABASE_URL", "postgresql+psycopg://social:social@localhost:5433/social"
)

engine = create_async_engine(DATABASE_URL)
