from uuid import UUID
import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.order import Order, OrderItem
from app.models.cart import Cart
from app.schemas.order import OrderCreate

async def create_order_from_cart(db: AsyncSession, user_id: UUID, order_in: OrderCreate) -> Order:
    cart = await db.scalar(select(Cart).where(Cart.user_id == user_id))
    if not cart or not cart.items:
        raise ValueError("Cart is empty")

    subtotal = sum(item.unit_price_snapshot * item.quantity for item in cart.items)

    order = Order(
        order_number=str(uuid.uuid4()).split('-')[0].upper(),
        user_id=user_id,
        shipping_address_id=order_in.shipping_address_id,
        billing_address_id=order_in.billing_address_id,
        status="pending",
        payment_status="pending",
        subtotal_amount=subtotal,
        total_amount=subtotal,
        notes=order_in.notes
    )
    db.add(order)
    await db.flush()

    for item in cart.items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            product_name_snapshot=item.product.name,
            sku_snapshot=item.product.sku,
            quantity=item.quantity,
            unit_price_snapshot=item.unit_price_snapshot,
            line_total=item.unit_price_snapshot * item.quantity
        )
        db.add(order_item)

    # Clear cart
    for item in cart.items:
        await db.delete(item)

    await db.commit()
    await db.refresh(order)
    return order
