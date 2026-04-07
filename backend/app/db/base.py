from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all ORM entities.
    SQLAlchemy 2.x style is preferred here because it is the current modern pattern.
    """
    pass
