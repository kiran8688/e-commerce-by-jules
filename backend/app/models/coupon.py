import uuid
from datetime import datetime
from sqlalchemy import Boolean, DateTime, Numeric, String, ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class Coupon(Base):
    __tablename__ = "coupons"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    code: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    discount_type: Mapped[str] = mapped_column(String(20), nullable=False)
    discount_value: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)
    minimum_order_amount: Mapped[float] = mapped_column(Numeric(12, 2), default=0)
    max_redemptions: Mapped[int | None] = mapped_column(Integer, nullable=True)
    redemptions_count: Mapped[int] = mapped_column(Integer, default=0)
    starts_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    ends_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

class OrderCoupon(Base):
    __tablename__ = "order_coupons"

    order_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("orders.id"), primary_key=True)
    coupon_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("coupons.id"), nullable=False)
    discount_amount: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)

    order = relationship("Order")
    coupon = relationship("Coupon")
