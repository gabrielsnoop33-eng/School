import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.infrastructure.database.models import Base

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./school.db")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def init_db() -> None:
    """Crée les tables si elles n'existent pas (utile en dev, à remplacer par des migrations Alembic en prod)."""
    Base.metadata.create_all(bind=engine)


def get_db_session() -> Session:
    session = SessionLocal()
    try:
        return session
    finally:
        pass