"""
MCP server for development and operational tasks.

Use this server to expose safe, bounded tools that help with:
- inspecting product/catalog data
- generating admin summaries
- reading docs and repository files
- supporting internal agent workflows

Keep business mutation tools narrow and authenticated.
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ecommerce-mcp")


@mcp.tool()
def summarize_catalog_health() -> str:
    """
    Return a textual summary of the current catalog state.

    In a real implementation, this tool would query the database and return
    counts for products, categories, low-stock items, and inactive products.
    """
    return "Catalog health summary placeholder"


@mcp.tool()
def draft_product_copy(name: str, features: list[str]) -> str:
    """
    Produce structured product-copy assistance for admin use.
    """
    return f"Draft copy for {name}: " + ", ".join(features)


if __name__ == "__main__":
    mcp.run()
