from Order_Project.pageObjects.dashboard import Dashboard


class Login:
    def __init__(self,page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self,username,password):
        self.page.locator("#userEmail").fill(username)
        self.page.locator("#userPassword").fill(password)
        self.page.locator("#login").click()
        db = Dashboard(self.page)
        return db