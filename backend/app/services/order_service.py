from uuid import UUID
import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.order import Order, OrderItem
from app.models.cart import Cart
from app.schemas.order import OrderCreate

async def create_order_from_cart(db: AsyncSession, user_id: UUID, order_in: OrderCreate) -> Order:
    """
    Transforms an active Cart into a finalized Order and clears the Cart.

    Design Decisions & Workflow:
    1.  **Validation:** We first verify the cart exists and has items. A user cannot checkout an empty cart.
    2.  **Calculations:** Subtotal is calculated server-side. *Never* trust client-provided totals.
    3.  **Snapshotting:** As the order items are created, we copy the current product details
        (name, sku, unit_price) directly from the cart item (which snapshots the product at add-time).
    4.  **Cleanup:** Once the order and its items are safely added to the session, we delete the cart items.

    Edge Cases:
    - What if a product's price changed while it was in the cart? Currently, `cart_items` store a
      `unit_price_snapshot` at the time of addition. To enforce current pricing, we would need
      to re-query the `Product` table here. For this MVP, we honor the price at the time they added it to the cart.
    - Concurrency: If two requests hit this simultaneously, `db.commit()` handles transaction integrity,
      though a distributed lock on `user_id` could be added for strict idempotency.
    """
    cart = await db.scalar(select(Cart).where(Cart.user_id == user_id))
    if not cart or not cart.items:
        raise ValueError("Cart is empty")

    # Always calculate totals on the server to prevent payload tampering.
    subtotal = sum(item.unit_price_snapshot * item.quantity for item in cart.items)

    # Generate a pseudo-random order number. In a real system, this might be a monotonic sequence
    # or follow a specific business format (e.g., ORD-2026-XXXXX).
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
