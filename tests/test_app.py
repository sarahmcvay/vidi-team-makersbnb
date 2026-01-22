from playwright.sync_api import Page, expect


"""
We can get the browsing page to load
"""
def test_get_spaces_browsing_page(page, test_web_address):
    page.goto(f'http://{test_web_address}/login')

    page.fill('input[name="email"]', 'test1@email.com')
    page.fill('input[name="password"]', 'test1password')

    page.click('button[type="login"]')
    page.goto(f'http://{test_web_address}/browsing_spaces')

"""
We can get the space 1 page to load
"""
def test_show_space(page, test_web_address):
    page.goto(f'http://{test_web_address}/login')

    page.fill('input[name="email"]', 'test1@email.com')
    page.fill('input[name="password"]', 'test1password')

    page.click('button[type="login"]')
    page.goto(f'http://{test_web_address}/show_space/1')
    
    h1_tag = page.get_by_role("heading", level=1)
    expect(h1_tag).to_have_text("Request a booking:")

"""
We can get the booking calendar to render
"""
def test_booking_calendar_renders(page, test_web_address):
    page.goto(f'http://{test_web_address}/login')

    page.fill('input[name="email"]', 'test1@email.com')
    page.fill('input[name="password"]', 'test1password')
    page.click('button[type="login"]')

    page.goto(f'http://{test_web_address}/show_space/1')

    page.click('#booking_range')
    expect(page.locator('.flatpickr-calendar')).to_be_visible()

"""
The pending date warns users during booking
"""
def test_pending_date_shows_warning(page, test_web_address):
    def test_pending_date_shows_warning(page, test_web_address):
        page.add_init_script("""
            window.pendingDates = ["2026-01-15"];
            window.approvedDates = [];
        """)
        page.goto(f'http://{test_web_address}/login')
        page.fill('input[name="email"]', 'test1@email.com')
        page.fill('input[name="password"]', 'test1password')
        page.click('button[type="login"]')

        page.goto(f'http://{test_web_address}/show_space/1')
        page.click('#booking_range')
        page.wait_for_selector('.flatpickr-calendar')
        pending_day = page.locator('.flatpickr-day.pending')
        expect(pending_day).to_have_count(1)
        pending_day.first.click()
        page.locator('.flatpickr-day:not(.disabled)').nth(1).click()
        expect(page.locator('#pendingMessage')).to_be_visible()

"""
We can create a space
"""

def test_post_create_space_submits_successfully(page, test_web_address):

    page.goto(f'http://{test_web_address}/login')
    page.fill('input[name="email"]', 'test1@email.com')
    page.fill('input[name="password"]', 'test1password')
    page.click('button[type="login"]')


    page.goto(f'http://{test_web_address}/create_space')


    page.fill('input[name="name"]', 'Test Space')
    page.fill('textarea[name="details"]', 'A cozy test space.')
    page.fill('input[name="price"]', '100')
    page.fill('input[name="img_link"]', 'https://example.com/image.jpg')

    page.click('button[type="submit"]')

    page.wait_for_selector("h2")

    space = page.locator("p", has_text="Test Space").last
    parent = space.locator("xpath=..")

    expect(parent).to_contain_text("Test Space")
    expect(parent).to_contain_text("A cozy test space.")
    expect(parent).to_contain_text("100.00")



"""
We can get the user_dashboard page to load
"""

def test_get_dashboard_page_to_load(page, test_web_address):
    page.goto(f'http://{test_web_address}/login')

    page.fill('input[name="email"]', 'test1@email.com')
    page.fill('input[name="password"]', 'test1password')

    page.click('button[type="login"]')

    page.goto(f'http://{test_web_address}/user_dashboard')
    
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text([
        "Spaces you own that require approval", 
        "Spaces you are visiting soon", 
        "Your Owned Spaces"
    ])

