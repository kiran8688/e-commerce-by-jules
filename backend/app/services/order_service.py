import uuid
from datetime import datetime
from uuid import UUID

from app.models.cart import Cart
from app.models.order import Order, OrderItem
from app.schemas.order import OrderCreate
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession


async def create_order_from_cart(db: AsyncSession, user_id: UUID, order_in: OrderCreate) -> Order:
    """
    Transforms an active Cart into a finalized Order and clears the Cart.

    Design Decisions & Workflow:
    1.  **Validation:** We first verify the cart exists and has items.
        A user cannot checkout an empty cart.
    2.  **Calculations:** Subtotal is calculated server-side.
        *Never* trust client-provided totals.
    3.  **Snapshotting:** As the order items are created, we copy the current product details
        (name, sku, unit_price) directly from the cart item
        (which snapshots the product at add-time).
    4.  **Cleanup:** Once the order and its items are safely added to the session,
        we delete the cart items.

    Edge Cases:
    - What if a product's price changed while it was in the cart? Currently, `cart_items` store a
      `unit_price_snapshot` at the time of addition. To enforce current pricing, we would need
      to re-query the `Product` table here. For this MVP, we honor the price at the time they
      added it to the cart.
    - Concurrency: If two requests hit this simultaneously, `db.commit()` handles transaction
      integrity, though a distributed lock on `user_id` could be added for strict idempotency.
    """
    cart = await db.scalar(select(Cart).where(Cart.user_id == user_id))
    if not cart or not cart.items:
        raise ValueError("Cart is empty")

    # Always calculate totals on the server to prevent payload tampering.
    subtotal = sum(item.unit_price_snapshot * item.quantity for item in cart.items)

    # Generate a monotonic order number in a business format: ORD-YYYY-XXXXX
    # We use a database sequence to ensure uniqueness and monotonicity.
    seq_result = await db.execute(text("SELECT nextval('order_number_seq')"))
    seq_value = seq_result.scalar()
    current_year = datetime.now().year
    order_number = f"ORD-{current_year}-{seq_value:05d}"

    order = Order(
        order_number=order_number,
        user_id=user_id,
        shipping_address_id=order_in.shipping_address_id,
        billing_address_id=order_in.billing_address_id,
        status="pending",
        payment_status="pending",
        subtotal_amount=subtotal,
        total_amount=subtotal,
        notes=order_in.notes,
    )
    db.add(order)
    await db.flush()

    order_items = [
        OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            product_name_snapshot=item.product.name,
            sku_snapshot=item.product.sku,
            quantity=item.quantity,
            unit_price_snapshot=item.unit_price_snapshot,
            line_total=item.unit_price_snapshot * item.quantity,
        )
        for item in cart.items
    ]
    db.add_all(order_items)

    # Clear cart
    for item in cart.items:
        await db.delete(item)

    await db.commit()
    await db.refresh(order)
    return order
