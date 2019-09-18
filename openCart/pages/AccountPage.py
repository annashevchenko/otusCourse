from openCart.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from openCart.locators.AccountLocations import AccountLocations
from openCart.locators.CatalogProductLocators import CatalogProductLocators
from openCart.logging_openCart import logger


class AccountPage(BasePage):
    # открываем меню в my_account
    def open_menu_my_account(self):
        logger.info("Открываем меню в My Account")
        self.driver.find_element_by_css_selector(AccountLocations.my_account_link).click()

    # указываем имя при регистрации
    def set_first_name_Register(self, text):
        logger.info("Указываем имя: " + text)
        self.driver.find_element(*AccountLocations.FIRSTNAME).send_keys(text)

    # указываем фамилию при регистрации
    def set_last_name_Register(self, text):
        logger.info("Указываем фамилию: " + text)
        self.driver.find_element(*AccountLocations.LASTNAME).send_keys(text)

    # указываем email при регистрации
    def set_email_Register(self, text):
        logger.info("Указываем email: " + text)
        self.driver.find_element(*AccountLocations.EMAIL).send_keys(text)

    # указываем телефон при регистрации
    def set_phone_Register(self, text):
        logger.info("Указываем телефон: " + text)
        self.driver.find_element(*AccountLocations.PHONE).send_keys(text)

    # указываем пароль при регистрации
    def set_password_Register(self, text):
        logger.info("Указываем пароль: " + text)
        self.driver.find_element(*AccountLocations.PASSWORD).send_keys(text)

    # указываем подтверждение пароля при регистрации
    def set_comfirmPass_Register(self, text):
        logger.info("Подтверждаем пароль: " + text)
        self.driver.find_element(*AccountLocations.COMFIRMPASS).send_keys(text)

    # смотрим заголовки после авторизации
    def header_in_account(self):
        logger.info("Проверяем, что на странице есть следующие разделы")
        self.driver.find_element_by_xpath(AccountLocations.header_in_account.format("My Account"))
        self.driver.find_element_by_xpath(AccountLocations.header_in_account.format("My Orders"))
        self.driver.find_element_by_xpath(AccountLocations.header_in_account.format("My Affiliate Account"))
        self.driver.find_element_by_xpath(AccountLocations.header_in_account.format("Newsletter"))

    # открываем раздел
    def open_section_in_account(self, text):
        logger.info("Открываем раздел: " + text)
        self.driver.find_element_by_xpath(AccountLocations.section.format(text)).click()

    # метод
    def set_first_name(self, text):
        logger.info("Указываем имя: " + text)
        self._input(*AccountLocations.FIRSTNAME, text)

    # ожидаем сообщение
    def wait_message(self):
        logger.info("Ожидаем сообщение: ")
        self._wait_element_(By.CSS_SELECTOR, CatalogProductLocators.mess_by_product)
