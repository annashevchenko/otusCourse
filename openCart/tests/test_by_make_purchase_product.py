import random
import string

import pymysql
import pytest

from openCart.locators.AccountLocations import AccountLocations
from openCart.pages.AccountPage import AccountPage
from openCart.pages.LoginPage import LoginPage
from openCart.pages.MainPage import MainPage
from openCart.pages.CustomerPage import CustomerPage


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


def test_customer_payment(browser, fixture_create_random_string, pytest_datebase_cursor):
    """Тест выполняет успешную авторизацию и проверяем разделы"""
    # добавляем в БД customer и выполняем авторизацию под ним
    pytest_datebase_cursor.execute('INSERT INTO oc_customer '
                                   '(customer_group_id, store_id, language_id, firstname, lastname,'
                                   'email, telephone, fax, password, salt, newsletter, address_id, custom_field, '
                                   'ip, status, safe, token, code, date_added) VALUES (1, 0, 1, "testcustomername",'
                                   '"testcustomersurname", "fefefe@yandex.ru", "+79115421236", "",'
                                   ' "7ff42bb705b77cb370d51a1d6b87a07a9f86aa3a", "PoBL6JJ56", 0, 0, " ", "172.20.0.1",'
                                   '1, 0, " ", " ", now())')
    # находим в БД customer запоминаем его id
    pytest_datebase_cursor.execute('select customer_id from oc_customer where firstname = "testcustomername"')
    for row in pytest_datebase_cursor:
        id_cus = str(row[0])
    # открываем раздел авторизации аккаунта
    AccountPage(browser).open_menu_my_account()
    browser.find_element_by_xpath(AccountLocations.my_account_Login).click()
    LoginPage(browser).login_on_page_email("fefefe@yandex.ru", "Qazwsx123")
    browser.find_element_by_link_text("Desktops").click()
    MainPage(browser).open_directory("Desktops")
    browser.find_element_by_link_text("Mac (1)").click()
    browser.find_element_by_link_text("iMac")
    MainPage(browser).click_add_cart()
    MainPage(browser).click_button_Checkout()
    CustomerPage(browser).set_customer_name_payment("testcustomername")
    CustomerPage(browser).set_customer_lastname_payment("testcustomername")
    CustomerPage(browser).set_customer_address_payment("Kievskay street, d. 1, kv. 243")
    CustomerPage(browser).set_customer_city_payment("Moscow")
    CustomerPage(browser).set_customer_postcode_payment("140132")
    CustomerPage(browser).select_customer_country_payment("Russian Federation")
    CustomerPage(browser).select_customer_region_payment("Moscow")
    CustomerPage(browser).button_Continue_address()
    CustomerPage(browser).checked_shipping_address()
    CustomerPage(browser).button_сontinue_ship_address()
    CustomerPage(browser).set_comment_customer_payment("this test order")
    CustomerPage(browser).button_Continue_ship_method()
    CustomerPage(browser).checkbox_agree()
    CustomerPage(browser).button_Continue_pay_method()
    CustomerPage(browser).button_Confirm_Order()
    MainPage(browser).product_header_order_place("Your order has been placed!")
    MainPage(browser).button_сontinue()
    # удаляем customer в БД
    pytest_datebase_cursor.execute('delete from oc_customer where customer_id = "' + id_cus + '"')
