import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(record_video_dir="videos/")
        page = await context.new_page()

        await page.goto('http://localhost:5173/cart')

        # Wait for the breadcrumb to be visible
        await page.wait_for_selector('nav[aria-label="Breadcrumb"]')

        # Take a screenshot of the page
        await page.screenshot(path='breadcrumb_cart_screenshot.png', full_page=True)

        await context.close()
        await browser.close()

asyncio.run(main())
