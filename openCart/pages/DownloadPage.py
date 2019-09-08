from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

from openCart.pages.BasePage import BasePage
from openCart.locators.MainLocators import MainLocators
from openCart.locators.DownLoadLocators import DownLoadLocators
from openCart.locators.ProductCartLocators import ProductCartLocators
from selenium.webdriver.common.by import By


class DownloadPage(BasePage):
    # вводим в поле поиска текст
    def add_new_download(self):
        self.driver.find_element_by_css_selector(DownLoadLocators.button_add_new_download).click()

    # указываем наименование загрузки
    def set_download_name(self, text):
        self.driver.find_element_by_css_selector(DownLoadLocators.download_name).send_keys(text)

    # указываем наименование файла
    def set_file_name(self, text):
        self.driver.find_element_by_css_selector(DownLoadLocators.file_name).send_keys(text)

    # указываем наименование маски
    def set_mask_name(self, text):
        self.driver.find_element_by_css_selector(DownLoadLocators.mask_name).send_keys(text)

        # указываем файл для загрузки
    def set_input_file(self, text):
        self.driver.find_element_by_css_selector(DownLoadLocators.file).send_keys(text)

    # нажимаем кнопку сохранить загрузку
    def save_download(self):
        self.driver.find_element_by_css_selector(DownLoadLocators.button_save_download).click()

    # находим загруженный файл по наименованию загрузки
    def find_dowload_name(self, text):
        self.driver.find_element_by_xpath(DownLoadLocators.find_name_download.format(text))
