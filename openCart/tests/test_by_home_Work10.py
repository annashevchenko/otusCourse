import time

import pytest
import string
import random

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from openCart.locators.LoginLocators import LoginLocators
from openCart.locators.CatalogProductLocators import CatalogProductLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


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
    driver.find_element_by_css_selector(LoginLocators.button_login).click()


def test_open_other_page_in_product_list(driver, url_admin, fixture_authorization_admin):
    """Тест переходит на другую страницу в Product List"""
    driver.find_element_by_id("menu-catalog").click()
    # открываем каталог и заходим в Products
    count = 0
    while count < 10:
        try:
            driver.find_element_by_link_text("Products").click()
            break
        except NoSuchElementException:
            count += 1
            time.sleep(1)
    # нажимаем на страницу 2
    driver.find_element_by_xpath(CatalogProductLocators.pagination_in_productList.format("2")).click()
    # проверяем, что вторая страница стала активной
    driver.find_element_by_xpath(CatalogProductLocators.active_page.format("2"))


def test_delete_product_in_catalog_with_wait(driver, url_admin, fixture_authorization_admin):
    """Тест удаляет под админом  продукт в каталоге"""
    # открываем каталог и заходим в Products
    driver.find_element_by_id("menu-catalog").click()
    # открываем каталог и заходим в Products
    count = 0
    while count < 10:
        try:
            driver.find_element_by_link_text("Products").click()
            break
        except NoSuchElementException:
            count += 1
            time.sleep(1)
    # указываем значения для поиска в форме фильтра:  стоимость продуктов, фильтруемся по нулевой стоимости
    filter_product_price = driver.find_element_by_id("input-price")
    filter_product_price.click()
    filter_product_price.send_keys("0.00")
    driver.find_element_by_id("button-filter").click()
    # находим и записываем в список все checkbox в списке, устанавливаем первый
    checkbox = driver.find_elements_by_css_selector(CatalogProductLocators.checkbox_in_productList)
    checkbox[0].click()
    # нажимаем кнопку удалить, подтверждаем удаление, проверям наличие сообщение об успешной операции
    driver.find_element_by_css_selector(CatalogProductLocators.button_delete_product).click()
    Alert(driver).accept()
    # ожидаем 1 секунду и проверяем, сообщение, об успешно выполненной операции
    wait = WebDriverWait(driver, 1)
    # находим сообщение об успешно выполненной операции
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")))


def test_filter_products_in_catalog_with_wait(driver, url_admin, fixture_authorization_admin):
    """Тест выполняет фильтрацию продуктов в каталоге под админом"""
    # открываем каталог и заходим в Products
    driver.find_element_by_id("menu-catalog").click()
    # открываем каталог и заходим в Products
    count = 0
    while count < 10:
        try:
            driver.find_element_by_link_text("Products").click()
            break
        except NoSuchElementException:
            count += 1
            time.sleep(1)
    # указываем значения для поиска в форме фильтра: наименование продукта(ищем по контекстному поиску), модель, стоимость,
    # количество и статус
    filter_product_name = driver.find_element_by_id("input-name")
    filter_product_name.click()
    filter_product_name.send_keys("Apple")
    WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[style='top: 133px; left: 31px; display: block;']")))
    driver.find_element_by_link_text("Apple Cinema 30\"").click()
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
    driver.find_element_by_xpath(CatalogProductLocators.product_in_productList.format("Apple Cinema 30\""))


def test_edit_product_in_catalog_with_wait(driver, url_admin, fixture_authorization_admin):
    """Тест редактирует под админом  продукт в каталоге"""
    # открываем каталог и заходим в Products
    driver.find_element_by_id("menu-catalog").click()
    # открываем каталог и заходим в Products
    count = 0
    while count < 10:
        try:
            driver.find_element_by_link_text("Products").click()
            break
        except NoSuchElementException:
            count += 1
            time.sleep(1)
    # указываем значения для поиска в форме фильтра:  стоимость продуктов, фильтруемся по нулевой стоимости
    filter_product_price = driver.find_element_by_id("input-price")
    filter_product_price.click()
    filter_product_price.send_keys("0.00")
    driver.find_element_by_id("button-filter").click()
    # находим и записываем в список все кнопки Edit в списке, нажимаем на первую кнопку
    buttons_edit = driver.find_elements_by_css_selector(CatalogProductLocators.buttons_edit_in_productList)
    buttons_edit[0].click()
    # переходитм в раздел Data и изменяем цену на рандомную
    driver.find_element_by_link_text("Data").click()
    product_price = driver.find_element_by_id("input-price")
    product_price.click()
    product_price.clear()
    price = ''.join(random.choice(string.digits) for _ in range(3))
    product_price.send_keys(price)
    # переходитм в раздел Image и нажимаем на иконку с изображение
    driver.find_element_by_link_text("Image").click()
    driver.find_element_by_id("thumb-image").click()
    # ожидаем появление элемента с интрументами по управлению изображением
    # нажимаем кнопку редактировать
    driver.find_element_by_id("button-image").click()
    # ожидаем форму управление изображением нажимаем на demo для выбора изображения
    WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[id='modal-image'][style='display: block;']")))
    driver.find_element_by_css_selector("a[class='directory']").click()
    WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a img[title='gift-voucher-b irthday.jpg']")))
    driver.find_element_by_css_selector("a img[title='gift-voucher-b irthday.jpg']").click()
    # нажимаем кнопку сохранить и проверям наличие сообщение об успешной операции
    driver.find_element_by_css_selector(CatalogProductLocators.button_save_new_product).click()
    wait = WebDriverWait(driver, 1)
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")))
