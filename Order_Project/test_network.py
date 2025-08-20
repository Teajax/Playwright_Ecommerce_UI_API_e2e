#mock api to get the desired edge case test
#intercepting response call with route
#fulfill method to test the edge case
import pytest
from playwright.sync_api import Page

fakePayloadOrderResponse = {"data":[], "message": "No Orders"}
def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )

@pytest.mark.smoke
def test_network_1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.locator("#userEmail").fill("rahulshetty@gmail.com")
    page.locator("#userPassword").fill("Iamking@000")
    page.locator("#login").click()
    page.get_by_role("button", name="ORDERS").click()
    msg = page.locator(".mt-4").text_content()
    print(msg)