from openCart.pages.BasePage import BasePage
from openCart.locators.MainLocators import MainLocators
from openCart.locators.ProductCartLocators import ProductCartLocators
from selenium.webdriver.common.by import By
from openCart.logging_openCart import logger


class MainPage(BasePage):
    # вводим в поле поиска текст
    def set_in_search(self, text):
        logger.info("Вводим в поле поиска текст: " + text)
        self.driver.find_element_by_css_selector(MainLocators.search).send_keys(text)

    # нажимаем кнопку поиска
    def click_button_search(self):
        logger.info("Нажимаем кнопку поиска")
        self.driver.find_element_by_css_selector(MainLocators.search_button).click()

    # нажимаем ссылку на наименовании продукта
    def click_product_link(self, text):
        logger.info("Нажимаем ссылку на наименовании продукта")
        self.driver.find_element_by_xpath(MainLocators.product).click()

    # нажимаем кнопку добавить в корзину
    def click_add_cart(self):
        logger.info("Нажимаем добавить в корзину")
        self.driver.find_element_by_xpath(MainLocators.add_to_cart).click()

    # нажимаем на содержимое корзины
    def click_item_cart(self):
        logger.info("Нажимаем на содержимое корзины")
        self.driver.find_element_by_css_selector(MainLocators.item_cart).click()

    # нажимаем на Checkout
    def click_button_Checkout(self):
        logger.info("Нажимаем на Checkout")
        self.driver.find_element_by_xpath(MainLocators.button_Checkout).click()

    # нажимаем корзину
    def click_cart(self):
        logger.info("Нажимаем на корзину")
        self.driver.find_element(*MainLocators.CART).click()

    # открываем директорию
    def open_directory(self, text):
        logger.info("Открываем директорию: " + text)
        self._wait_element_(By.XPATH, MainLocators.open_menu.format(text))

    # открывает карточку
    def open_product_cart(self, text):
        logger.info("Открываем карточку: " + text)
        self.driver.find_element_by_css_selector(ProductCartLocators.image_in_cart_by_name.format(text)).click()

    # находим наименование карточки по названию
    def product_header_cart_by_name(self, text):
        logger.info("Находим наименование карточки: " + text)
        self.driver.find_element_by_xpath(ProductCartLocators.header_cart_by_name.format(text))

    # ожидаем сообщение
    def wait_message(self):
        logger.info("Ожидаем сообщение")
        self._wait_element_(By.CSS_SELECTOR, MainLocators.mess)

    # закрываем информационное сообщение
    def button_close_mess(self):
        logger.info("Закрываем информационное сообщение")
        self.driver.find_element_by_css_selector(MainLocators.button_close_mess).click()

    # находим Shopping Cart
    def shopping_cart(self):
        logger.info("Находим Shopping Cart и кликаем по нему")
        self.driver.find_element_by_css_selector(MainLocators.shopping_cart).click()

    # находим сообщение об успешно выполненном заказе
    def product_header_order_place(self, text):
        logger.info("Находим сообщение об успешно выполненном заказе : " + text)
        self.driver.find_element_by_xpath(MainLocators.heading.format(text))

    # находим кнопку продолжить
    def button_сontinue(self):
        logger.info("Находим кнопку продолжить")
        self.driver.find_element_by_xpath(MainLocators.сontinue)

