import pytest
from openCart.pages.LoginPage import LoginPage
from openCart.pages.CatalogPage import CatalogPage
from openCart.logging_openCart import logger


@pytest.fixture()
def url_admin(browser, request):
    """эта фикстура возвращает url для входа в openCart под админом"""
    url = 'admin/'
    return browser.get("".join([request.config.getoption("--url"), url]))


@pytest.fixture()
def fixture_authorization_admin(browser, url_admin):
    """эта фикстура выполняет авторизацию под админом"""
    LoginPage(browser).login_on_page("user", "bitnami1")


def test_open_product_catalog_with_log_browser(browser, fixture_authorization_admin):
    """Тест открывает раздел products в catalog и выаодит логи браузера"""
    # открываем каталог и заходим в Products
    CatalogPage(browser).open_catalog()
    CatalogPage(browser).wait_section_in_menu_navigation("Products")
    browser.find_element_by_link_text("Products").click()
    logger.info("виды логов нашел следующие: ")
    logger.info(browser.log_types)
    log = browser.get_log("browser")
    logger.info("в данных логах следующая информация")
    logger.info(log)
