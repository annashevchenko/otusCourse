import pytest
from selenium.webdriver.common.by import By
import string
import random
from openCart.locators import MainPage
from openCart.locators import ProductCartPage
from openCart.locators import LoginPage
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def fixture_create_random_string():
    """эта фикстура создает произвольную строку из строчных и заглавных букв и цифр"""
    string_random1 = ''.join(random.choice(string.ascii_uppercase) for _ in range(1))
    string_random2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    string_random = string_random1 + string_random2
    return string_random



def test_seach_by_text(driver):
    """Тест находит поле поиска, вводит в поле данны для поиска, нажимает кнопку найти. Находит заголовок результат поиска"""
    find_text = "mac"
    element = driver.find_element_by_css_selector(MainPage.seach)
    element.click()
    element.send_keys(find_text)
    driver.find_element_by_css_selector(MainPage.seach_button).click()
    driver.find_element_by_xpath("*//h1[text()='Search - " + find_text + "']")




def test_open_by_directory(driver):
    """Тест открывает меню Desktops->Mac"""
    ActionChains(driver).move_to_element(driver.find_element_by_link_text("Desktops")).click().pause(0.5).perform()
    driver.find_element_by_xpath(MainPage.open_menu.format("Desktops"))
    driver.find_element_by_link_text("Mac (1)").click()
    driver.find_element_by_xpath(MainPage.menu_mac.format("Mac"))




def test_open_product_cart(driver):
    """Тест открывает карточку продукта -> монитор Apple Cinema 30\""""
    ActionChains(driver).move_to_element(driver.find_element_by_link_text("Components")).click().pause(0.5).perform()
    driver.find_element_by_xpath(MainPage.open_menu.format("Components"))
    driver.find_element_by_link_text("Monitors (2)").click()
    driver.find_element_by_css_selector(ProductCartPage.image_in_cart_by_name.format("Apple Cinema 30\"")).click()
    driver.find_element_by_xpath(ProductCartPage.header_cart_by_name.format("Apple Cinema 30\""))



def test_open_product_cart_add_in_wishList(driver):
    """Тест открывает карточку продукта ->Mонитор Apple Cinema 30\" и добавляет его в wishList"""
    ActionChains(driver).move_to_element(driver.find_element_by_link_text("Components")).click().pause(0.5).perform()
    driver.find_element_by_xpath(MainPage.open_menu.format("Components"))
    driver.find_element_by_link_text("Monitors (2)").click()
    driver.find_element_by_css_selector(ProductCartPage.image_in_cart_by_name.format("Apple Cinema 30\"")).click()
    driver.find_element_by_css_selector(ProductCartPage.button_WishList).click()




def test_register_new_account(driver, fixture_create_random_string):
    """Тест открывает форму регистрации, заполняет поля и регистрирует новый аккаунт"""
    driver.find_element_by_css_selector(LoginPage.top_element.format("My Account")).click()
    driver.find_element_by_link_text("Register").click()
    firstname = driver.find_element_by_id("input-firstname")
    firstname.click()
    firstname.send_keys(fixture_create_random_string)
    lastname = driver.find_element_by_id("input-lastname")
    lastname.click()
    lastname.send_keys(fixture_create_random_string)
    email = driver.find_element_by_id("input-email")
    email.click()
    mail = ''.join(random.choice(string.ascii_lowercase) for _ in range(15))
    email.send_keys(''.join(random.choice(string.ascii_lowercase) for _ in range(15)) + "@yandex.ru")
    phone = driver.find_element_by_id("input-telephone")
    phone.click()
    phone_num = ''.join(random.choice(string.digits) for _ in range(10))
    phone.send_keys("+7" + phone_num)
    password = driver.find_element_by_id("input-password")
    password.click()
    password.send_keys("Qazwsx123")
    password_confirm = driver.find_element_by_id("input-confirm")
    password_confirm.click()
    password_confirm.send_keys("Qazwsx123")
    driver.find_element_by_css_selector(LoginPage.subscribe.format("1"))
    driver.find_element_by_name("agree").click()
    driver.find_element_by_css_selector(LoginPage.сontinue).click()
    driver.find_element_by_xpath(LoginPage.message_in_header.format("Your Account Has Been Created!"))
    driver.find_element_by_css_selector(LoginPage.сontinue_account_created).click()
    driver.find_element_by_xpath(LoginPage.header_in_account.format("My Account"))





