import pytest
from selenium import webdriver
from openCart.locators import CustomerLocations, LoginLocators
from openCart.pages import CustomerPage, LoginPage

desired_cap = {
    'browser': 'Chrome',
    'browser_version': '75.0',
    'os': 'Windows',
    'os_version': '10',
    'resolution': '1024x768',
    'name': 'Bstack-[Python] Sample Test'
}


@pytest.fixture()
def driver():
    browser = webdriver.Remote(
        command_executor='http://bsuser53852:xp6oyQJSVmXHaFzenfsY@hub.browserstack.com:80/wd/hub',
        desired_capabilities=desired_cap)
    yield browser
    browser.quit()
