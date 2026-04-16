"""
MCP server for development and operational tasks.

Use this server to expose safe, bounded tools that help with:
- inspecting product/catalog data
- generating admin summaries
- reading docs and repository files
- supporting internal agent workflows

Keep business mutation tools narrow and authenticated.
"""

from app.db.session import AsyncSessionLocal
from app.models.catalog import Category, Inventory, Product
from mcp.server.fastmcp import FastMCP
from sqlalchemy import func, select

mcp = FastMCP("ecommerce-mcp")


@mcp.tool()
async def summarize_catalog_health() -> str:
    """
    Return a textual summary of the current catalog state.

    Queries the database to return counts for products, categories,
    and identify low-stock items.
    """
    async with AsyncSessionLocal() as session:
        # Count total products
        product_count_stmt = select(func.count()).select_from(Product)
        product_count = (await session.execute(product_count_stmt)).scalar() or 0

        # Count active products
        active_product_stmt = select(func.count()).select_from(Product).where(Product.is_active == True)
        active_count = (await session.execute(active_product_stmt)).scalar() or 0

        # Count total categories
        category_count_stmt = select(func.count()).select_from(Category)
        category_count = (await session.execute(category_count_stmt)).scalar() or 0

        # Identify low stock items (quantity <= reorder_level)
        low_stock_stmt = (
            select(func.count())
            .select_from(Inventory)
            .where(Inventory.quantity_on_hand <= Inventory.reorder_level)
        )
        low_stock_count = (await session.execute(low_stock_stmt)).scalar() or 0

    return (
        f"Catalog Health Summary:\n"
        f"- Total Products: {product_count}\n"
        f"- Active Products: {active_count}\n"
        f"- Total Categories: {category_count}\n"
        f"- Low Stock Items: {low_stock_count}"
    )


@mcp.tool()
def draft_product_copy(name: str, features: list[str]) -> str:
    """
    Produce structured product-copy assistance for admin use.
    """
    feature_list = "\n".join([f"- {f}" for f in features])
    return (
        f"Draft copy for {name}:\n\n"
        f"Experience the ultimate in quality with our new {name}. "
        f"Designed for those who value both style and substance.\n\n"
        f"Key Features:\n{feature_list}\n\n"
        f"Order yours today and elevate your lifestyle!"
    )


if __name__ == "__main__":
    mcp.run()
