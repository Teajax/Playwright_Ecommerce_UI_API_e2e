from playwright.sync_api import expect


class orderDetails:
    def __init__(self,page):
        self.page = page

    def checkOrderMsg(self):
        expect(self.page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")