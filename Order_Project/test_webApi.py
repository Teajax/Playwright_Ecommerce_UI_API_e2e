import json

import pytest
from playwright.async_api import Playwright
from Order_Project.utils.apibase import apiUtils
from Order_Project.pageObjects.login import Login
from Order_Project.pageObjects.orderHistory import orderHistory
from Order_Project.pageObjects.orderDetails import orderDetails

with open("Order_Project/data/credentials.json") as f:
    test_data = json.load(f)
    #print(test_data)
    user_cred = test_data.get("user-credentials")

@pytest.mark.parametrize("user_credentials",user_cred)
def test_e2e_web_api(playwright:Playwright,browserInstance,user_credentials):
    username = user_credentials.get("user-email")
    password = user_credentials.get("user-password")


    #create order -- > orderId
    apiutils = apiUtils()
    orderid = apiutils.createOrder(playwright,user_credentials)

    #login
    login = Login(browserInstance)
    login.navigate()
    db = login.login(username,password)
    db.orderNavigate()
    #orderpage --> order is present
    order = orderHistory(browserInstance)
    order.selectOrder(orderid)

    orderdetail = orderDetails(browserInstance)
    orderdetail.checkOrderMsg()
