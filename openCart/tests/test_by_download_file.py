import pytest
import string
import random
import os

from selenium.webdriver import ActionChains
from openCart.pages.LoginPage import LoginPage
from openCart.pages.CatalogPage import CatalogPage
from openCart.pages.DownloadPage import DownloadPage
from openCart.locators.DownLoadLocators import DownLoadLocators
from openCart.pages.MainPage import MainPage


@pytest.fixture()
def url_admin(browser, request):
    """эта фикстура возвращает url для входа в openCart под админом"""
    url = 'admin/'
    return browser.get("".join([request.config.getoption("--url"), url]))


@pytest.fixture()
def fixture_authorization_admin(browser, url_admin):
    """эта фикстура выполняет авторизацию под админом"""
    LoginPage(browser).login_on_page("user", "bitnami1")


def test_add_download_file(browser, fixture_authorization_admin):
    """Тест добавляет под админом новый продукт в каталог"""
    # открываем каталог и заходим в Products
    CatalogPage(browser).open_catalog()
    CatalogPage(browser).wait_section_in_menu_navigation("Downloads")
    browser.find_element_by_link_text("Downloads").click()
    # нажимаем кнопку создать новую загрузку файла
    DownloadPage(browser).add_new_download()
    # указываем наименование загрузки и нажимаем кнопку upload
    download_name = "this is download " + ''.join(random.choice(string.digits) for _ in range(5))
    DownloadPage(browser).set_download_name(download_name)
    browser.find_element_by_css_selector(DownLoadLocators.button_upload).click()
    # находим файл
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'ee67d5e51ec5993dea7c065e064fd8c5.jpg')
    # после нажатия кнопки upload на форме появляется нужный input type=file, передаем ему нащ файл
    DownloadPage(browser).set_input_file(filename)
    DownloadPage(browser).set_file_name(filename)
    # ждем и переключаемся на alert, подтверждаем на не загрузку
    ActionChains(browser).pause(0.5).perform()
    browser.switch_to.alert.accept()
    # нажимаем сохранить и ждем сообщение об успешной загрузки
    DownloadPage(browser).save_download()
    MainPage(browser).wait_message()
    DownloadPage(browser).find_dowload_name(download_name)
