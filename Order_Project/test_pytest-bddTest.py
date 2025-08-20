import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from Order_Project.pageObjects.login import Login
from Order_Project.pageObjects.orderDetails import orderDetails
from Order_Project.pageObjects.orderHistory import orderHistory
from Order_Project.utils.apibase import apiUtils

scenarios("feature/orderTransaction.feature")

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('place the item order with {username} and {password}'))
def placeOrder(playwright,username, password,shared_data):
    apiutils = apiUtils()
    user_cred = {}
    user_cred['user-email'] = username
    user_cred['user-password'] = password
    print(user_cred)
    orderid = apiutils.createOrder(playwright,user_cred)
    shared_data['orderid'] = orderid

@given('the user is on landing page')
def landingPage(browserInstance,shared_data):
    login = Login(browserInstance)
    login.navigate()
    shared_data['login'] = login

@when(parsers.parse('I login to portal with {username} and {password}'))
def login(username, password,shared_data):
    db = shared_data['login'].login(username, password)
    shared_data['db'] = db

@when('navigate to order page')
def navigate_orderpage(shared_data):
    db= shared_data['db']
    db.orderNavigate()

@when('select to order page')
def select_orderpage(browserInstance,shared_data):
    order = orderHistory(browserInstance)
    orderid = shared_data['orderid']
    order.selectOrder(orderid)

@then('order message is successfully displayed')
def order_message(browserInstance):
    orderdetail = orderDetails(browserInstance)
    orderdetail.checkOrderMsg()