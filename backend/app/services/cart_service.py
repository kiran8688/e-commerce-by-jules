from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.cart import Cart, CartItem
from app.models.catalog import Product
from app.schemas.cart import CartItemCreate

def get_or_create_cart(db: Session, user_id: UUID) -> Cart:
    cart = db.scalar(select(Cart).where(Cart.user_id == user_id))
    if not cart:
        cart = Cart(user_id=user_id)
        db.add(cart)
        db.commit()
        db.refresh(cart)
    return cart

def add_to_cart(db: Session, user_id: UUID, item: CartItemCreate) -> Cart:
    cart = get_or_create_cart(db, user_id)
    product = db.scalar(select(Product).where(Product.id == item.product_id))
    if not product:
        raise ValueError("Product not found")

    cart_item = db.scalar(
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

    db.commit()
    db.refresh(cart)
    return cart
