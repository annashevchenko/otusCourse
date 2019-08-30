from openCart.pages.BasePage import BasePage
from openCart.locators.LoginLocators import LoginLocators

class LoginPage(BasePage):

    def __set_username(self, text_username):
        self.username = self.driver.find_element_by_id("input-username")
        self.username.click
        self.username.send_keys(text_username)

    def __set_password(self, text_password):
        self.password = self.driver.find_element_by_id("input-password")
        self.password.click()
        self.password.send_keys(text_password)

    def login_on_page(self, username, password):
        self.__set_username(username)
        self.__set_password(password)
        self.driver.find_element_by_css_selector(LoginLocators.button_login).click()