from __future__ import annotations

from collections.abc import Generator, Iterator

from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import DATABASE_URL


class Base(DeclarativeBase):
    pass


# Engine owns the connection pool
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)


# Session factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


# ORM session dependency (per request)
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Raw SQL connection dependency (per usage)
def get_connection() -> Iterator[Connection]:
    with engine.begin() as connection:
        yield connection
