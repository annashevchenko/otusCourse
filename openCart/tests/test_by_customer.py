import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from openCart.locators import CustomerLocations
from openCart.pages import CustomerPage, LoginPage





@pytest.fixture()
def url_admin(browser, request):
    """эта фикстура возвращает url для входа в openCart под админом"""
    url = 'admin/'
    return browser.get("".join([request.config.getoption("--url"), url]))


@pytest.fixture()
def fixture_authorization_admin(browser, url_admin):
    """эта фикстура выполняет авторизацию под админом"""
    LoginPage(browser).login_on_page("user", "bitnami1")


def test_filter_customer(browser, fixture_authorization_admin):
    """Тест выполняет фильтрацию клиентов под админом"""
    # открываем раздел клиентов и заходим в Customers
    CustomerPage(browser).open_customer()
    CustomerPage(browser).wait_section_in_menu_navigation("Customers")
    browser.find_element_by_xpath(CustomerLocations.customers).click()
    CustomerPage(browser).set_customer_name_in_filter("Fid")
    CustomerPage(browser).wait_menu()
    browser.find_element_by_link_text("Fidzsncmikv Fidzsncmikv").click()
    CustomerPage(browser).set_customer_email("vgmvwqfdfldztvl@yandex.ru")
    CustomerPage(browser).set_customer_group_in_filter("Default")
    CustomerPage(browser).set_customer_status_in_filter("Enabled")
    CustomerPage(browser).set_customer_ip("172.19.0.1")
    CustomerPage(browser).set_customer_date_added("2019-08-21")
    CustomerPage(browser).button_filter()
    CustomerPage(browser).find_filter_element("Fidzsncmikv Fidzsncmikv")




