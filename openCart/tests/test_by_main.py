import random
import string
import pytest
from openCart.pages.MainPage import MainPage
from openCart.locators.MainLocators import MainLocators
from openCart.locators.ProductCartLocators import ProductCartLocators


@pytest.fixture
def fixture_create_random_string():
    """эта фикстура создает произвольную строку из строчных и заглавных букв и цифр"""
    string_random1 = ''.join(random.choice(string.ascii_uppercase) for _ in range(1))
    string_random2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    string_random = string_random1 + string_random2
    return string_random


@pytest.mark.env("regression")
def test_seach_by_text(browser):
    """Тест находит поле поиска, вводит в поле данны для поиска, нажимает кнопку найти. Находит заголовок результат поиска"""
    find_text = "mac"
    MainPage(browser).set_in_search(find_text)
    MainPage(browser).click_button_search()
    browser.find_element_by_xpath(MainLocators.search_result.format(find_text))


@pytest.mark.env("regression")
def test_empty_cart(browser):
    """Тест находит пустую корзину, нажимает на нее и получает сообщение"""
    MainPage(browser).click_cart
    browser.find_element_by_xpath(MainLocators.cart_text.format("Your shopping cart is empty!"))
    browser.get_log('browser')


@pytest.mark.env("regression")
def test_open_by_directory(browser):
    """Тест открывает меню Desktops->Mac"""
    browser.find_element_by_link_text("Desktops").click()
    MainPage(browser).open_directory("Desktops")
    browser.find_element_by_link_text("Mac (1)").click()
    browser.find_element_by_link_text("iMac")


@pytest.mark.env("regression")
@pytest.mark.env("smoke")
def test_open_product_cart(browser):
    """Тест открывает карточку продукта -> монитор Apple Cinema 30\""""
    browser.find_element_by_link_text("Components").click()
    MainPage(browser).open_directory("Components")
    browser.find_element_by_link_text("Monitors (2)").click()
    MainPage(browser).open_product_cart("Apple Cinema 30\"")
    MainPage(browser).product_header_cart_by_name("Apple Cinema 30\"")


@pytest.mark.env("regression")
@pytest.mark.env("smoke")
def test_open_product_cart_add_in_wishList(browser):
    """Тест открывает карточку продукта ->Mонитор Apple Cinema 30\" и добавляет его в wishList"""
    browser.find_element_by_link_text("Components").click()
    MainPage(browser).open_directory("Components")
    browser.find_element_by_link_text("Monitors (2)").click()
    MainPage(browser).open_product_cart("Apple Cinema 30\"")
    browser.find_element_by_css_selector(ProductCartLocators.button_WishList).click()
