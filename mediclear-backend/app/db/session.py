from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.core.config import settings
class Base(DeclarativeBase):
    """Shared declarative base so all ORM models register under one metadata object."""
    pass

# Engine manages the connection pool to PostgreSQL
engine = create_engine(settings.database_url, pool_pre_ping=True)

# SessionLocal acts as a factory for per-request database sessions
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    """FastAPI dependency that yields a DB session per request and closes it cleanly."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()