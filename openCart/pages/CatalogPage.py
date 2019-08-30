from selenium.common.exceptions import NoSuchElementException

from openCart.pages.BasePage import BasePage
from openCart.locators import CatalogProductLocators
import time


class CatalogPage(BasePage):

    # метод ожидает отображение раздела в меню навигации
    def open_section_in_menu_navigation(self, text_section):
        count = 0
        while count < 10:
            try:
                self.driver.find_element_by_link_text(text_section).click()
                break
            except NoSuchElementException:
                count += 1
                time.sleep(1)

    # метод вводит в фильтре значение price (стоимость)
    def set_product_price_in_filter(self, text_price):
        self.filter_product_price = self.driver.find_element_by_id("input-price")
        self.filter_product_price.click()
        self.filter_product_price.send_keys(text_price)

    # метод вводит в фильтре значение product_name (наименование)
    def set_product_name_in_filter(self, text_product_name):
        self.filter_product_name = self.driver.find_element_by_id("input-name")
        self.filter_product_name.click()
        self.filter_product_name.send_keys(text_product_name)


    # метод вводит в фильтре значение product_model (модель)
    def set_product_model_in_filter(self, text_product_model):
        self.filter_product_model = self.driver.find_element_by_id("input-model")
        self.filter_product_model.click()
        self.filter_product_model.send_keys(text_product_model)


    # метод вводит в фильтре значение product_quantity (количество)
    def set_product_quantity_in_filter(self, text_product_quantity):
        self.filter_product_quantity = self.driver.find_element_by_id("input-quantity")
        self.filter_product_quantity.click()
        self.filter_product_quantity.send_keys(text_product_quantity)


    # метод вводит значение price в разделе Date
    def set_product_price(self, text_price):
        self.product_price = self.driver.find_element_by_id("input-price")
        self.product_price.click()
        self.product_price.clear()
        self.product_price.send_keys(text_price)




