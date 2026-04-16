import uuid
from datetime import datetime

from app.db.base import Base
from sqlalchemy import Boolean, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    """
    Represents an application user (both customers and admins).

    Design Decisions:
    - We use UUIDs for primary keys to prevent exposing internal row counts (e.g., user #12)
      and to allow distributed systems to generate IDs without database round-trips.
    - Password hashes are stored instead of plain text for security.
    - `is_admin` is a simple boolean flag. For a more complex enterprise system,
      this would likely be replaced by an RBAC (Role-Based Access Control) join table,
      but a boolean is sufficient and performant for this e-commerce spec.

    Relationships:
    - lazy="selectin": This is strictly required for async SQLAlchemy compatibility.
      It ensures that when a `User` is queried, the related data is loaded via a secondary
      SELECT statement immediately, preventing implicit synchronous queries (which crash async).
    - cascade="all, delete-orphan": Ensures that if a User is deleted, all their addresses
      and their cart are also wiped from the DB to prevent orphaned records.
    """
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    full_name: Mapped[str] = mapped_column(String(200), nullable=False)
    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan", lazy="selectin")
    orders = relationship("Order", back_populates="user", lazy="selectin")
    reviews = relationship("Review", back_populates="user", lazy="selectin")
    cart = relationship("Cart", back_populates="user", uselist=False, cascade="all, delete-orphan", lazy="selectin")


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    label: Mapped[str | None] = mapped_column(String(100), nullable=True)
    recipient_name: Mapped[str] = mapped_column(String(200), nullable=False)
    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)
    line1: Mapped[str] = mapped_column(String(255), nullable=False)
    line2: Mapped[str | None] = mapped_column(String(255), nullable=True)
    city: Mapped[str] = mapped_column(String(120), nullable=False)
    state: Mapped[str] = mapped_column(String(120), nullable=False)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=False)
    country_code: Mapped[str] = mapped_column(String(2), nullable=False)
    is_default_shipping: Mapped[bool] = mapped_column(Boolean, default=False)
    is_default_billing: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    user = relationship("User", back_populates="addresses", lazy="selectin")
