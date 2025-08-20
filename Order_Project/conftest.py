import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browsername",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser selection",
    )

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

@pytest.fixture(scope="function")
def browserInstance(playwright,request):
    browserName = request.config.getoption("browsername")
    if browserName == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browserName == "firefox":
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()