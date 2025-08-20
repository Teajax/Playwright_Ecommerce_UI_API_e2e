class orderHistory:
    def __init__(self,page):
        self.page = page

    def selectOrder(self,orderid):
        row = self.page.locator("tr").filter(has_text=orderid)
        row.get_by_role("button", name="View").click()