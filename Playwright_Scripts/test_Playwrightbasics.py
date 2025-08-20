import pytest
from playwright.sync_api import Playwright,Page #if you want auto suggestions with intelligence
import time
def test_playwrightbasic(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/")

@pytest.mark.smoke
#chromium browser , with headless mode - can directly use page fixture
def test_playwrightshortcut(page:Page):
    page.goto("https://rahulshettyacademy.com/")

def test_corelocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.locator("#terms").check()
    page.get_by_role("combobox").select_option("teach")
    page.locator("#signInBtn").click()
    time.sleep(5)

def test_openfirefox(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/")