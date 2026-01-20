from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    p_tag = page.locator(".navbar")

    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_contain_text

"""
We can get the browsing page to load
"""
def test_get_spaces_browsing_page(page, test_web_address):
    page.goto(f'http://{test_web_address}/browsing_spaces')

    p_tag = page.locator("h1")
    expect(p_tag).to_have_text("List of Spaces")
    
def test_show_space(page, test_web_address):
    page.goto(f'http://{test_web_address}/show_space/1')
    
    p_tag = page.locator("h1")
    
    expect(p_tag).to_have_text('space1')