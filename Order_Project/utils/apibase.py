from http.client import responses

from playwright.sync_api import Playwright

url1 = "/api/ecom/auth/login"
url2 = "/api/ecom/order/create-order"
order_payload = {"orders":[{"country":"India","productOrderedId":"67a8dde5c0d3e6622a297cc8"}]}

class apiUtils:
    def getToken(self,playwright:Playwright,user_credentials):
        user_email = user_credentials["user-email"]
        user_password = user_credentials["user-password"]
        print(user_email,user_password)
        api_req = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        login_payload = {"userEmail": user_email, "userPassword": user_password}
        response = api_req.post(url1,
                                data=login_payload,
                                headers={
                                    "Content-Type":"application/json"})
        token = response.json()["token"]
        return token

    def createOrder(self,playwright:Playwright,user_credentials):
        token = self.getToken(playwright,user_credentials)
        api_req_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")

        response = api_req_context.post(url2,
                             data=order_payload,
                             headers={"Authorization": token,
                                      "Content-Type": "application/json"
                                      })
        response_body = response.json()
        orderid = response_body["orders"][0]
        return orderid


