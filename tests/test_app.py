from playwright.sync_api import Page, expect


"""
We can get the browsing page to load
"""
def test_get_spaces_browsing_page(page, test_web_address):
    page.goto(f'http://{test_web_address}/login')

    page.fill('input[name="name"]', 'test1')
    page.fill('input[name="email"]', 'test1@email.com')
    page.fill('input[name="password"]', 'test1password')

    page.click('button[type="login"]')
    page.goto(f'http://{test_web_address}/browsing_spaces')

    
def test_show_space(page, test_web_address):
    page.goto(f'http://{test_web_address}/login')

    page.fill('input[name="name"]', 'test1')
    page.fill('input[name="email"]', 'test1@email.com')
    page.fill('input[name="password"]', 'test1password')

    page.click('button[type="login"]')
    page.goto(f'http://{test_web_address}/show_space/1')
    
    h1_tag = page.get_by_role("heading", level=1)
    expect(h1_tag).to_have_text("Request a booking:")


"""
We can get the user_dashboard page to load
"""

def test_get_dashboard_page_to_load(page, test_web_address):
    page.goto(f'http://{test_web_address}/login')

    page.fill('input[name="name"]', 'test1')
    page.fill('input[name="email"]', 'test1@email.com')
    page.fill('input[name="password"]', 'test1password')

    page.click('button[type="login"]')

    page.goto(f'http://{test_web_address}/user_dashboard')
    
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text([
        "Your Approval Required", 
        "Your Upcoming Bookings", 
        "Your Owned Spaces"
    ])

