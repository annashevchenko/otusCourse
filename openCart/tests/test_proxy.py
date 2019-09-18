import urllib  #
import pytest
from browsermobproxy import Server, Client
from selenium import webdriver
from openCart.pages.MainPage import MainPage
from openCart.locators.MainLocators import MainLocators
from openCart.logging_openCart import logger

server = Server()
server.start()
client = Client("localhost:8080")
client.port
client.new_har()


@pytest.fixture()
def browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    url = urllib.parse.urlparse(client.proxy).path
    options.add_argument('--proxy-server=%s' % url)
    driver = webdriver.Chrome(options=options)
    request.addfinalizer(driver.quit)
    return driver


def test_empty_cart(browser):
    """Тест находит пустую корзину, нажимает на нее и получает сообщение"""
    browser.get("http://localhost/")
    MainPage(browser).click_cart
    browser.find_element_by_xpath(MainLocators.cart_text.format("Your shopping cart is empty!"))
    browser.get_log('browser')
    logger.info("лог через proxy: ")
    logger.info(client.har)
