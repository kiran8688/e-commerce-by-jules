from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import noload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.cart import Cart, CartItem
from app.models.catalog import Product
from app.schemas.cart import CartItemCreate

async def get_or_create_cart(db: AsyncSession, user_id: UUID) -> Cart:
    # ⚡ Bolt: Prevent unnecessary eager loading of the User model since it is not returned in CartOut
    cart = await db.scalar(select(Cart).where(Cart.user_id == user_id).options(noload(Cart.user)))
    if not cart:
        cart = Cart(user_id=user_id)
        db.add(cart)
        await db.commit()
        await db.refresh(cart)
    return cart

async def add_to_cart(db: AsyncSession, user_id: UUID, item: CartItemCreate) -> Cart:
    cart = await get_or_create_cart(db, user_id)
    # ⚡ Bolt: Prevent N+1 eager loading of heavy product relationships (images, reviews, inventory) since only base product fields are needed for CartItem creation
    product = await db.scalar(select(Product).where(Product.id == item.product_id).options(noload('*')))
    if not product:
        raise ValueError("Product not found")

    cart_item = await db.scalar(
        select(CartItem).where(CartItem.cart_id == cart.id, CartItem.product_id == item.product_id)
    )

    if cart_item:
        cart_item.quantity += item.quantity
    else:
        cart_item = CartItem(
            cart_id=cart.id,
            product_id=product.id,
            quantity=item.quantity,
            unit_price_snapshot=product.price
        )
        db.add(cart_item)

    await db.commit()
    await db.refresh(cart)
    return cart
