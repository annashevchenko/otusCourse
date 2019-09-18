from openCart.pages.BasePage import BasePage
from openCart.locators.DownLoadLocators import DownLoadLocators
from openCart.logging_openCart import logger


class DownloadPage(BasePage):
    # вводим в поле поиска текст
    def add_new_download(self):
        logger.info("Нажимаем кнопку новая загрузка")
        self.driver.find_element_by_css_selector(DownLoadLocators.button_add_new_download).click()

    # указываем наименование загрузки
    def set_download_name(self, text):
        logger.info("Указываем наименование загрузки: " + text)
        self.driver.find_element_by_css_selector(DownLoadLocators.download_name).send_keys(text)

    # указываем наименование файла
    def set_file_name(self, text):
        logger.info("Указываем наименование файла: " + text)
        self.driver.find_element_by_css_selector(DownLoadLocators.file_name).send_keys(text)

    # указываем наименование маски
    def set_mask_name(self, text):
        logger.info("Указываем маску: " + text)
        self.driver.find_element_by_css_selector(DownLoadLocators.mask_name).send_keys(text)

    # указываем файл для загрузки
    def set_input_file(self, text):
        logger.info("Указываем файл для загрузки: " + text)
        self.driver.find_element_by_css_selector(DownLoadLocators.file).send_keys(text)

    # нажимаем кнопку сохранить загрузку
    def save_download(self):
        logger.info("Нажимаем кнопку сохранить")
        self.driver.find_element_by_css_selector(DownLoadLocators.button_save_download).click()

    # находим загруженный файл по наименованию загрузки
    def find_dowload_name(self, text):
        logger.info("Находим загруженный файл по наименованию загрузки: " + text)
        self.driver.find_element_by_xpath(DownLoadLocators.find_name_download.format(text))
