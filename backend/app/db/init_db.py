import asyncio
import logging
import random
import uuid

import app.models.cart
import app.models.catalog
import app.models.coupon
import app.models.order
import app.models.payment
import app.models.review

# Import all models so Base.metadata can create tables
import app.models.user
from app.core.security import hash_password
from app.db.base import Base
from app.db.session import AsyncSessionLocal, engine
from sqlalchemy import select

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def create_tables() -> None:
    async with engine.begin() as conn:
        logger.info("Creating all tables...")
        await conn.run_sync(Base.metadata.create_all)

async def init_db() -> None:
    async with AsyncSessionLocal() as session:
        # Create Admin User
        admin_email = "admin@example.com"
        result = await session.execute(select(app.models.user.User).where(app.models.user.User.email == admin_email))
        user = result.scalars().first()
        if not user:
            logger.info("Creating admin user...")
            admin_user = app.models.user.User(
                id=uuid.uuid4(),
                email=admin_email,
                hashed_password=hash_password("adminpassword"),
                full_name="System Administrator",
                is_active=True,
                is_admin=True,
            )
            session.add(admin_user)
            await session.commit()
            logger.info(f"Admin user created with email: {admin_email} and password: adminpassword")
        else:
            logger.info("Admin user already exists.")

        # Create Categories
        categories_data = [
            {"name": "Electronics", "slug": "electronics", "desc": "Gadgets and devices."},
            {"name": "Apparel", "slug": "apparel", "desc": "Clothing and accessories."},
            {"name": "Home & Garden", "slug": "home-garden", "desc": "Items for your home."},
            {"name": "Sports", "slug": "sports", "desc": "Sporting goods and equipment."},
            {"name": "Books", "slug": "books", "desc": "Literature and non-fiction."}
        ]

        category_objs = []
        for cat_data in categories_data:
            result = await session.execute(select(app.models.catalog.Category).where(app.models.catalog.Category.slug == cat_data["slug"]))
            cat = result.scalars().first()
            if not cat:
                cat = app.models.catalog.Category(
                    id=uuid.uuid4(),
                    name=cat_data["name"],
                    slug=cat_data["slug"],
                    description=cat_data["desc"]
                )
                session.add(cat)
                category_objs.append(cat)

        if category_objs:
            await session.commit()
            logger.info(f"Created {len(category_objs)} categories.")
        else:
            result = await session.execute(select(app.models.catalog.Category))
            category_objs = list(result.scalars().all())

        if not category_objs:
            logger.warning("No categories available to attach products to.")
            return

        # Create Dummy Products
        result = await session.execute(select(app.models.catalog.Product).limit(1))
        existing_product = result.scalars().first()

        if not existing_product:
            logger.info("Generating dummy products...")
            adjectives = ["Premium", "Essential", "Luxury", "Smart", "Eco-Friendly", "Pro", "Ultra", "Classic", "Modern", "Vintage"]
            nouns = {
                "Electronics": ["Smartphone", "Laptop", "Headphones", "Speaker", "Watch", "Tablet"],
                "Apparel": ["T-Shirt", "Jacket", "Sneakers", "Jeans", "Hoodie", "Hat"],
                "Home & Garden": ["Planter", "Lamp", "Chair", "Desk", "Rug", "Vase"],
                "Sports": ["Yoga Mat", "Dumbbells", "Water Bottle", "Running Shoes", "Tent", "Backpack"],
                "Books": ["Novel", "Guide", "Cookbook", "Journal", "Biography", "Atlas"]
            }

            for i in range(1, 51):  # Generate 50 products
                cat = random.choice(category_objs)
                base_noun = random.choice(nouns.get(cat.name, ["Item"]))
                adj = random.choice(adjectives)
                name = f"{adj} {base_noun} {i}"
                slug = name.lower().replace(" ", "-") + f"-{uuid.uuid4().hex[:6]}"
                sku = f"{cat.name[:3].upper()}-{uuid.uuid4().hex[:8].upper()}"
                price = round(random.uniform(19.99, 499.99), 2)

                product = app.models.catalog.Product(
                    id=uuid.uuid4(),
                    category_id=cat.id,
                    name=name,
                    slug=slug,
                    sku=sku,
                    short_description=f"A fantastic {name.lower()} for your daily needs.",
                    description=f"Detailed description for {name}. This product features high-quality materials and exceptional craftsmanship. Perfect for anyone looking for a reliable {base_noun.lower()}.",
                    price=price,
                    compare_at_price=round(price * 1.2, 2) if random.random() > 0.7 else None,
                    is_active=True,
                    is_featured=random.random() > 0.8
                )
                session.add(product)

                # Add Inventory
                inventory = app.models.catalog.Inventory(
                    id=uuid.uuid4(),
                    product_id=product.id,
                    quantity_on_hand=random.randint(10, 500),
                    reorder_level=10
                )
                session.add(inventory)

                # Add Image
                image = app.models.catalog.ProductImage(
                    id=uuid.uuid4(),
                    product_id=product.id,
                    image_url=f"https://picsum.photos/seed/{product.id}/600/800",
                    alt_text=f"Image of {name}",
                    is_primary=True
                )
                session.add(image)

            await session.commit()
            logger.info("Created 50 dummy products with inventory and images.")
        else:
             logger.info("Products already exist in the database.")


async def main() -> None:
    logger.info("Starting database initialization...")
    await create_tables()
    await init_db()
    logger.info("Database initialization finished.")

if __name__ == "__main__":
    asyncio.run(main())
