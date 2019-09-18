from openCart.pages.BasePage import BasePage
from openCart.locators.LoginLocators import LoginLocators
from openCart.logging_openCart import logger


class LoginPage(BasePage):

    def __set_username(self, text_username):
        logger.info("находим поле Username")
        self.username = self.driver.find_element_by_id("input-username")
        logger.info("Кликаем по полю")
        self.username.click
        logger.info("Воодим в поле: " + text_username)
        self.username.send_keys(text_username)
        return self

    def __set_useremail(self, text_useremail):
        logger.info("находим поле useremail")
        self.useremail = self.driver.find_element_by_id("input-email")
        logger.info("Кликаем по полю")
        self.useremail.click
        logger.info("Воодим в поле: " + text_useremail)
        self.useremail.send_keys(text_useremail)
        return self

    def __set_password(self, text_password):
        logger.info("находим поле password")
        self.password = self.driver.find_element_by_id("input-password")
        logger.info("Кликаем по полю")
        self.password.click()
        logger.info("Воодим в поле: " + text_password)
        self.password.send_keys(text_password)
        return self

    def login_on_page(self, username, password):
        logger.info("находим поле Username и вводим данные: " + username)
        self.__set_username(username)
        logger.info("находим поле Password и вводим данные: " + password)
        self.__set_password(password)
        logger.info("выполняет вход, по кнопке login")
        self.driver.find_element_by_css_selector(LoginLocators.button_login).click()
        return self

    def login_on_page_email(self, useremail, password):
        logger.info("находим поле Useremail и вводим данные: " + useremail)
        self.__set_useremail(useremail)
        logger.info("находим поле Password и вводим данные: " + password)
        self.__set_password(password)
        logger.info("выполняет вход, по кнопке login")
        self.driver.find_element_by_css_selector(LoginLocators.button_user_login).click()
        return self
