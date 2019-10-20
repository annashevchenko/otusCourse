import random
import string

import pymysql
import pytest

from openCart.locators.AccountLocations import AccountLocations
from openCart.pages.AccountPage import AccountPage
from openCart.pages.LoginPage import LoginPage
from openCart.pages.MainPage import MainPage


@pytest.fixture()
def pytest_datebase_cursor():
    conn = pymysql.connect(host='localhost', user='bn_opencart', db='bitnami_opencart')
    cursor = conn.cursor()

    yield cursor
    cursor.close()
    conn.close()


@pytest.fixture
def fixture_create_random_string():
    """эта фикстура создает произвольную строку из строчных и заглавных букв и цифр"""
    string_random1 = ''.join(random.choice(string.ascii_uppercase) for _ in range(1))
    string_random2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    string_random = string_random1 + string_random2
    return string_random


def test_register_new_account(browser, fixture_create_random_string, pytest_datebase_cursor):
    """Тест открывает форму регистрации, заполняет поля и регистрирует новый аккаунт"""
    # открываем раздел регистрации нового аккаунта
    mail = ''.join(random.choice(string.ascii_lowercase) for _ in range(15))
    phone_num = ''.join(random.choice(string.digits) for _ in range(10))
    AccountPage(browser).open_menu_my_account()
    browser.find_element_by_xpath(AccountLocations.my_account_Register).click()
    # указываем регистрационне данные
    name = fixture_create_random_string
    surname = fixture_create_random_string
    AccountPage(browser).set_first_name_Register(name)
    AccountPage(browser).set_last_name_Register(surname)
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
    # находим пользователя в БД
    pytest_datebase_cursor.execute("select * from oc_customer where firstname = " + name + " and lastname = " + surname + " and status = 1")


def test_login_account(browser, fixture_create_random_string, pytest_datebase_cursor):
    """Тест выполняет успешную авторизацию и проверяем разделы"""
    # находим в БД customer и выполняем авторизацию под ним
    pytest_datebase_cursor.execute("select email from oc_customer where  status = 1 LIMIT 1")
    for row in pytest_datebase_cursor:
        email = row[0]
    # открываем раздел авторизации аккаунта
    AccountPage(browser).open_menu_my_account()
    browser.find_element_by_xpath(AccountLocations.my_account_Login).click()
    LoginPage(browser).login_on_page_email(email, "Qazwsx123")
    AccountPage(browser).header_in_account()


def test_my_account_information_edit_firstName(browser, fixture_create_random_string, pytest_datebase_cursor):
    """Тест выполняет успешную авторизацию и изменяем имя в разделе персональной информации"""
    # находим в БД customer и выполняем авторизацию под ним
    pytest_datebase_cursor.execute("select email, firstname, customer_id from oc_customer where  status = 1 LIMIT 1")
    for row in pytest_datebase_cursor:
        email = row[0]
        id_cus = str(row[2])
    # открываем раздел авторизации аккаунта
    AccountPage(browser).open_menu_my_account()
    browser.find_element_by_xpath(AccountLocations.my_account_Login).click()
    LoginPage(browser).login_on_page_email(email, "Qazwsx123")
    AccountPage(browser).open_section_in_account("Edit your account information")
    new_name = fixture_create_random_string
    AccountPage(browser).set_first_name(new_name)
    browser.find_element(*AccountLocations.CONTINUE).click()
    MainPage(browser).wait_message()
    # проверяем, что имя кастомера изменилось
    pytest_datebase_cursor.execute("select * from oc_customer where customer_id = '" + id_cus + "' and firstname = '" + new_name + "'")


