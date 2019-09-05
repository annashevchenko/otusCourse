import random
import string
import pytest

from openCart.pages.AccountPage import AccountPage
from openCart.locators.AccountLocations import AccountLocations
from openCart.pages.LoginPage import LoginPage
from openCart.pages.MainPage import MainPage


@pytest.fixture
def fixture_create_random_string():
    """эта фикстура создает произвольную строку из строчных и заглавных букв и цифр"""
    string_random1 = ''.join(random.choice(string.ascii_uppercase) for _ in range(1))
    string_random2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    string_random = string_random1 + string_random2
    return string_random


def test_register_new_account(browser, fixture_create_random_string):
    """Тест открывает форму регистрации, заполняет поля и регистрирует новый аккаунт"""
    # открываем раздел регистрации нового аккаунта
    mail = ''.join(random.choice(string.ascii_lowercase) for _ in range(15))
    phone_num = ''.join(random.choice(string.digits) for _ in range(10))
    AccountPage(browser).open_menu_my_account()
    browser.find_element_by_xpath(AccountLocations.my_account_Register).click()
    # указываем регистрационне данные
    AccountPage(browser).set_first_name_Register(fixture_create_random_string)
    AccountPage(browser).set_last_name_Register(fixture_create_random_string)
    AccountPage(browser).set_email_Register(mail + "@yandex.ru")
    AccountPage(browser).set_phone_Register("+7" + phone_num)
    AccountPage(browser).set_password_Register("Qazwsx123")
    AccountPage(browser).set_comfirmPass_Register("Qazwsx123")
    # соглашаемся на подписку, соглашаемся с политикой и нажимаем продолжить
    browser.find_element_by_css_selector(AccountLocations.subscribe.format("1"))
    browser.find_element(*AccountLocations.POLITICPRIVACY).click()
    browser.find_element(*AccountLocations.CONTINUE).click()
    # проверяем, что аккаунт успешно создался
    browser.find_element_by_xpath(AccountLocations.message_in_header.format("Your Account Has Been Created!"))
    browser.find_element_by_css_selector(AccountLocations.сontinue_account_created).click()
    browser.find_element_by_xpath(AccountLocations.header_in_account.format("My Account"))

