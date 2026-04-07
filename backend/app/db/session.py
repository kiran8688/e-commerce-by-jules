from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings

# sync engine because the stack requested SQLAlchemy + FastAPI in a straightforward production path
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,  # protects against stale PostgreSQL connections
    pool_size=10,
    max_overflow=20,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=Session,
)


def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency that provides one database session per request.

    Why this is important:
    - prevents connection leakage
    - keeps transaction scope explicit
    - ensures close() always runs
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
