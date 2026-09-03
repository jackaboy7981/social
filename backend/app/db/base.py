# base.py
# Shared SQLAlchemy declarative base. All module models inherit from this so
# a single metadata object exists for Alembic autogenerate to target.
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
