
class Dashboard:
    def __init__(self,page):
        self.page = page

    def orderNavigate(self):
        self.page.get_by_role("button", name="ORDERS").click()
