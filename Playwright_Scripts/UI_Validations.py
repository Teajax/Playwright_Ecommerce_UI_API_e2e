from playwright.sync_api import Page

def test_dynamicSelection(page:Page):
    #add items into cart - Iphone X, Nokia Edge
    #also verify cart shows 2items
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.locator("#terms").check()
    page.get_by_role("combobox").select_option("teach")
    page.locator("#signInBtn").click()

def test_handlenewtab(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as popup:
        page.locator(".blinkingText").click()
        childPage = popup.value
        text = childPage.locator(".red").text_content()
        print(text)

    