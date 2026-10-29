from playwright.sync_api import sync_playwright

def run_cuj(page):
    page.goto("http://localhost:5173/auth")
    page.wait_for_timeout(1000)

    # Fill email
    page.locator("#email").fill("test@example.com")
    page.wait_for_timeout(500)

    # Focus the password field to show it's active
    page.locator("#password").focus()
    page.wait_for_timeout(500)

    # Fill password
    page.locator("#password").fill("secret123")
    page.wait_for_timeout(500)

    # Hover the show password button to demonstrate the new hover state
    page.get_by_role("button", name="Show password").hover()
    page.wait_for_timeout(1000)

    # Click to show password
    page.get_by_role("button", name="Show password").click()
    page.wait_for_timeout(1000)

    # Hover again after clicking
    page.get_by_role("button", name="Hide password").hover()
    page.wait_for_timeout(500)

    # Take screenshot at the key moment showing the hover state
    page.screenshot(path="/home/jules/verification/screenshots/auth_verification.png")
    page.wait_for_timeout(1000)  # Hold final state for the video

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()  # MUST close context to save the video
            browser.close()
