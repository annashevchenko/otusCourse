import pytest
from selenium.webdriver.common.by import By
import string
import random
from openCart.locators import MainPage
from openCart.locators import ProductCartPage
from openCart.locators import LoginPage
from openCart.locators import CatalogProductPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert


@pytest.fixture
def fixture_create_random_string():
    """эта фикстура создает произвольную строку из строчных и заглавных букв и цифр"""
    string_random1 = ''.join(random.choice(string.ascii_uppercase) for _ in range(1))
    string_random2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    string_random = string_random1 + string_random2
    return string_random


@pytest.fixture(scope="session")
def url_admin(driver, request):
    """эта фикстура возвращает url для входа в openCart под админом"""
    url = 'admin/'
    return driver.get("".join([request.config.getoption("--url"), url]))


@pytest.fixture(scope="session")
def fixture_authorization_admin(driver, url_admin):
    """эта фикстура выполняет авторизацию под админом"""
    username = driver.find_element_by_id("input-username")
    username.click()
    username.send_keys("user")
    password = driver.find_element_by_id("input-password")
    password.click()
    password.send_keys("bitnami1")
    driver.find_element_by_css_selector(LoginPage.button_login).click()


def test_add_new_product_in_catalog(driver, fixture_authorization_admin, fixture_create_random_string):
    """Тест добавляет под админом новый продукт в каталог"""
    # открываем каталог и заходим в Products
    driver.find_element_by_id("menu-catalog").click()
    ActionChains(driver).pause(0.5).perform()
    driver.find_element_by_link_text("Products").click()
    # нажимаем кнопку добавить новый продукт
    driver.find_element_by_css_selector(CatalogProductPage.button_add_new).click()
    # вводим  поля: имя, описание, метатег, модель
    product_name = driver.find_element_by_name("product_description[1][name]")
    product_name.click()
    name = fixture_create_random_string + (''.join(random.choice(string.digits) for _ in range(10)))
    product_name.send_keys(name)
    product_description = driver.find_element_by_css_selector(CatalogProductPage.description_product)
    product_description.click()
    product_description.send_keys("This is autoTesting description New Product in Catalog")
    meta_tag = driver.find_element_by_name("product_description[1][meta_title]")
    meta_tag.click()
    meta_tag.send_keys(name)
    driver.find_element_by_link_text("Data").click()
    model = driver.find_element_by_name("model")
    model.click()
    model.send_keys("Product" + (''.join(random.choice(string.digits) for _ in range(5))))
    # нажимаем кнопку сохранить и проверям наличие сообщение об успешной операции
    driver.find_element_by_css_selector(CatalogProductPage.button_save_new_product).click()
    ActionChains(driver).pause(0.5).perform()
    driver.find_element_by_css_selector(CatalogProductPage.mess_by_product)


def test_filter_products_in_catalog(driver, fixture_authorization_admin, fixture_create_random_string):
    """Тест выполняет фильтрацию продуктов в каталоге под админом"""
    # открываем каталог и заходим в Products
    driver.find_element_by_id("menu-catalog").click()
    ActionChains(driver).pause(0.5).perform()
    driver.find_element_by_link_text("Products").click()
    # указываем значения для поиска в форме фильтра: наименование продукта(ищем по контекстному поиску), модель, стоимость,
    # количество и статус
    filter_product_name = driver.find_element_by_id("input-name")
    filter_product_name.click()
    filter_product_name.send_keys("Apple")
    ActionChains(driver).pause(0.5).perform()
    driver.find_element_by_css_selector(CatalogProductPage.menu_search_context)
    driver.find_element_by_link_text("Apple Cinema 30\"").click()
    filter_product_model = driver.find_element_by_id("input-model")
    filter_product_model.click();
    filter_product_model.send_keys("Product 15")
    filter_product_price = driver.find_element_by_id("input-price")
    filter_product_price.click()
    filter_product_price.send_keys("100")
    filter_product_quantity = driver.find_element_by_id("input-quantity")
    filter_product_quantity.click()
    filter_product_quantity.send_keys("990")
    filter_product_status = Select(driver.find_element_by_id("input-status"))
    filter_product_status.select_by_visible_text("Enabled")
    # нажимаем кнопку Filter и проверяем, что в списке продуктов есть продукт с указанным наименованием
    driver.find_element_by_id("button-filter").click()
    driver.find_element_by_xpath(CatalogProductPage.product_in_productList.format("Apple Cinema 30\""))


def test_delete_product_in_catalog(driver, fixture_authorization_admin):
    """Тест удаляет под админом  продукт в каталоге"""
    # открываем каталог и заходим в Products
    driver.find_element_by_id("menu-catalog").click()
    ActionChains(driver).pause(0.5).perform()
    driver.find_element_by_link_text("Products").click()
    # указываем значения для поиска в форме фильтра:  стоимость продуктов, фильтруемся по нулевой стоимости
    filter_product_price = driver.find_element_by_id("input-price")
    filter_product_price.click()
    filter_product_price.send_keys("0.00")
    driver.find_element_by_id("button-filter").click()
    # находим и записываем в список все checkbox в списке, устанавливаем первый
    checkbox = driver.find_elements_by_css_selector(CatalogProductPage.checkbox_in_productList)
    checkbox[0].click()
    # нажимаем кнопку удалить, подтверждаем удаление, проверям наличие сообщение об успешной операции
    driver.find_element_by_css_selector(CatalogProductPage.button_delete_product).click()
    Alert(driver).accept()
    ActionChains(driver).pause(0.5).perform()
    driver.find_element_by_css_selector(CatalogProductPage.mess_by_product)


def test_edit_product_in_catalog(driver, fixture_authorization_admin):
    """Тест редактирует под админом  продукт в каталоге"""
    # открываем каталог и заходим в Products
    driver.find_element_by_id("menu-catalog").click()
    ActionChains(driver).pause(0.5).perform()
    driver.find_element_by_link_text("Products").click()
    # указываем значения для поиска в форме фильтра:  стоимость продуктов, фильтруемся по нулевой стоимости
    filter_product_price = driver.find_element_by_id("input-price")
    filter_product_price.click()
    filter_product_price.send_keys("0.00")
    driver.find_element_by_id("button-filter").click()
    # находим и записываем в список все кнопки Edit в списке, нажимаем на первую кнопку
    buttons_edit = driver.find_elements_by_css_selector(CatalogProductPage.buttons_edit_in_productList)
    buttons_edit[0].click()
    # переходитм в раздел Data и изменяем цену на рандомную
    driver.find_element_by_link_text("Data").click()
    product_price = driver.find_element_by_id("input-price")
    product_price.click()
    product_price.clear()
    price = ''.join(random.choice(string.digits) for _ in range(3))
    product_price.send_keys(price)
    # нажимаем кнопку сохранить и проверям наличие сообщение об успешной операции
    driver.find_element_by_css_selector(CatalogProductPage.button_save_new_product).click()
    ActionChains(driver).pause(0.5).perform()
    driver.find_element_by_css_selector(CatalogProductPage.mess_by_product)


def test_copy_product_in_catalog(driver, fixture_authorization_admin):
    """Тест копирует под админом  продукт в каталоге"""
    # открываем каталог и заходим в Products
    driver.find_element_by_id("menu-catalog").click()
    ActionChains(driver).pause(0.5).perform()
    driver.find_element_by_link_text("Products").click()
    # указываем значения для поиска в форме фильтра: наименование продукта
    filter_product_name = driver.find_element_by_id("input-name")
    filter_product_name.click()
    filter_product_name.send_keys("HP LP3065")
    driver.find_element_by_id("button-filter").click()
    # находим и записываем в список все checkbox в списке, устанавливаем первый,
    # запоминаем количество продуктов с данным наименованием
    checkbox = driver.find_elements_by_css_selector(CatalogProductPage.checkbox_in_productList)
    count_product = len(checkbox)
    checkbox[0].click()
    # нажимаем кнопку копировать, проверям наличие сообщение об успешной операции, закрываем сообщение
    driver.find_element_by_css_selector(CatalogProductPage.button_copy_product).click()
    ActionChains(driver).pause(0.5).perform()
    driver.find_element_by_css_selector(CatalogProductPage.mess_by_product)
    driver.find_element_by_css_selector(CatalogProductPage.button_close_mess).click()
    # находим и записываем в список все checkbox в списке, проверяем, что количество продукта увеличилось на 1
    checkbox_after = driver.find_elements_by_css_selector(CatalogProductPage.checkbox_in_productList)
    count_product_after = len(checkbox_after)
    count_product_after == count_product + 1
    # выбираем послений продукт и удаляем его, подтверждаем удаление, проверям наличие сообщение об успешной операции
    checkbox_after[-1].click()
    driver.find_element_by_css_selector(CatalogProductPage.button_delete_product).click()
    Alert(driver).accept()
    ActionChains(driver).pause(0.5).perform()
    driver.find_element_by_css_selector(CatalogProductPage.mess_by_product)
