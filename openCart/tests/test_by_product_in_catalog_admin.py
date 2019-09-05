import pytest
import string
import random
from selenium.webdriver.common.alert import Alert
from openCart.pages.LoginPage import LoginPage
from openCart.pages.CatalogPage import CatalogPage
from openCart.pages.MainPage import MainPage

@pytest.fixture
def fixture_create_random_string():
    """эта фикстура создает произвольную строку из строчных и заглавных букв и цифр"""
    string_random1 = ''.join(random.choice(string.ascii_uppercase) for _ in range(1))
    string_random2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    string_random = string_random1 + string_random2
    return string_random


@pytest.fixture()
def url_admin(browser, request):
    """эта фикстура возвращает url для входа в openCart под админом"""
    url = 'admin/'
    return browser.get("".join([request.config.getoption("--url"), url]))


@pytest.fixture()
def fixture_authorization_admin(browser, url_admin):
    """эта фикстура выполняет авторизацию под админом"""
    LoginPage(browser).login_on_page("user", "bitnami1")


def test_add_new_product_in_catalog(browser, fixture_authorization_admin, fixture_create_random_string):
    """Тест добавляет под админом новый продукт в каталог"""
    # открываем каталог и заходим в Products
    CatalogPage(browser).open_catalog()
    CatalogPage(browser).wait_section_in_menu_navigation("Products")
    browser.find_element_by_link_text("Products").click()
    # нажимаем кнопку добавить новый продукт
    CatalogPage(browser).button_add_new_product()
    # вводим  поля: имя, описание, метатег, модель
    name = fixture_create_random_string + (''.join(random.choice(string.digits) for _ in range(10)))
    CatalogPage(browser).set_product_name(name)
    CatalogPage(browser).set_product_description("This is autoTesting description New Product in Catalog")
    CatalogPage(browser).set_product_meta_tag(name)
    browser.find_element_by_link_text("Data").click()
    CatalogPage(browser).set_product_model("Product" + (''.join(random.choice(string.digits) for _ in range(5))))
    # нажимаем кнопку сохранить и проверям наличие сообщение об успешной операции
    CatalogPage(browser).save_product()
    MainPage(browser).wait_message()


def test_filter_products_in_catalog(browser, fixture_authorization_admin):
    """Тест выполняет фильтрацию продуктов в каталоге под админом"""
    # открываем каталог и заходим в Products
    CatalogPage(browser).open_catalog()
    CatalogPage(browser).wait_section_in_menu_navigation("Products")
    browser.find_element_by_link_text("Products").click()
    # указываем значения для поиска в форме фильтра: наименование продукта(ищем по контекстному поиску), модель, стоимость,
    # количество и статус
    CatalogPage(browser).set_product_name_in_filter("Apple")
    CatalogPage(browser).wait_menu()
    browser.find_element_by_link_text("Apple Cinema 30\"").click()
    CatalogPage(browser).set_product_model("Product 15")
    CatalogPage(browser).set_product_price_in_filter("100")
    CatalogPage(browser).set_product_quantity_in_filter("990")
    CatalogPage(browser).set_product_status_in_filter("Enabled")
    CatalogPage(browser).button_filter()
    CatalogPage(browser).find_filter_element("Apple Cinema 30\"")


def test_delete_product_in_catalog(browser, fixture_authorization_admin):
    """Тест удаляет под админом  продукт в каталоге"""
    # открываем каталог и заходим в Products
    CatalogPage(browser).open_catalog()
    CatalogPage(browser).wait_section_in_menu_navigation("Products")
    browser.find_element_by_link_text("Products").click()
    # указываем значения для поиска в форме фильтра:  стоимость продуктов, фильтруемся по нулевой стоимости
    CatalogPage(browser).set_product_price_in_filter("0.00")
    CatalogPage(browser).button_filter()
    # находим и записываем в список все checkbox в списке, устанавливаем первый
    CatalogPage(browser).set_checkbox_in_product_list()
    # нажимаем кнопку удалить, подтверждаем удаление, проверям наличие сообщение об успешной операции
    CatalogPage(browser).button_delete()
    Alert(browser).accept()
    MainPage(browser).wait_message()


def test_edit_product_in_catalog_price(browser, fixture_authorization_admin):
    """Тест редактирует под админом  продукт в каталоге"""
    # открываем каталог и заходим в Products
    CatalogPage(browser).open_catalog()
    CatalogPage(browser).wait_section_in_menu_navigation("Products")
    browser.find_element_by_link_text("Products").click()
    # указываем значения для поиска в форме фильтра:  стоимость продуктов, фильтруемся по нулевой стоимости
    CatalogPage(browser).set_product_price_in_filter("0.00")
    CatalogPage(browser).button_filter()
    # находим и записываем в список все кнопки Edit в списке, нажимаем на первую кнопку
    CatalogPage(browser).set_buttons_edit_in_product_list()
    # переходитм в раздел Data и изменяем цену на рандомную
    browser.find_element_by_link_text("Data").click()
    CatalogPage(browser).set_product_price(''.join(random.choice(string.digits) for _ in range(3)))
    # нажимаем кнопку сохранить и проверям наличие сообщение об успешной операции
    CatalogPage(browser).save_product()
    MainPage(browser).wait_message()


def test_edit_product_in_catalog_price_image(browser, fixture_authorization_admin):
    """Тест редактирует под админом  продукт в каталоге"""
    # открываем каталог и заходим в Products
    CatalogPage(browser).open_catalog()
    CatalogPage(browser).wait_section_in_menu_navigation("Products")
    browser.find_element_by_link_text("Products").click()
    # указываем значения для поиска в форме фильтра:  стоимость продуктов, фильтруемся по нулевой стоимости
    CatalogPage(browser).set_product_price_in_filter("0.00")
    CatalogPage(browser).button_filter()
    # находим и записываем в список все кнопки Edit в списке, нажимаем на первую кнопку
    CatalogPage(browser).set_buttons_edit_in_product_list()
    # переходитм в раздел Data и изменяем цену на рандомную
    browser.find_element_by_link_text("Data").click()
    CatalogPage(browser).set_product_price(''.join(random.choice(string.digits) for _ in range(3)))
    # переходитм в раздел Image и нажимаем на иконку с изображение
    browser.find_element_by_link_text("Image").click()
    browser.find_element_by_id("thumb-image").click()
    # ожидаем появление элемента с интрументами по управлению изображением
    # нажимаем кнопку редактировать нажимаем на demo для выбора изображения
    CatalogPage(browser).set_product_image()
    CatalogPage(browser).select_product_image("gift-voucher-b irthday.jpg")
    # нажимаем кнопку сохранить и проверям наличие сообщение об успешной операции
    CatalogPage(browser).save_product()
    MainPage(browser).wait_message()


