from openCart.pages.BasePage import BasePage
from openCart.locators.MainLocators import MainLocators
from openCart.locators.ProductCartLocators import ProductCartLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    # вводим в поле поиска текст
    def set_in_search(self, text):
        self.driver.find_element_by_css_selector(MainLocators.search).send_keys(text)

    # нажимаем кнопку поиска
    def click_button_search(self):
        self.driver.find_element_by_css_selector(MainLocators.search_button).click()

    # нажимаем корзину
    def click_cart(self):
        self.driver.find_element(*MainLocators.CART).click()

    # открываем директорию
    def open_directory(self, text):
        self._wait_element_(By.XPATH, MainLocators.open_menu.format(text))

    # открывает карточку
    def open_product_cart(self, text):
        self.driver.find_element_by_css_selector(ProductCartLocators.image_in_cart_by_name.format(text)).click()

    # находим наименование карточки по названию
    def product_header_cart_by_name(self, text):
        self.driver.find_element_by_xpath(ProductCartLocators.header_cart_by_name.format(text))

    # ожидаем сообщение
    def wait_message(self):
        self._wait_element_(By.CSS_SELECTOR, MainLocators.mess)

    # закрываем информационное сообщение
    def button_close_mess(self):
        self.driver.find_element_by_css_selector(MainLocators.button_close_mess).click()
