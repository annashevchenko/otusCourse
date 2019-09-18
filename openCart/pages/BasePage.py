import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openCart.logging_openCart import logger


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def _wait_element_with_sleep(self, by, selector, num_count=10, num_sleep=1):
        count = 0
        while count < num_count:
            try:
                logger.info("Ожидаем на странице элемент")
                self.driver.find_element(by, selector)
                break

            except NoSuchElementException:
                logger.info("Элемент на странице не найден")
                count += 1
                time.sleep(num_sleep)

    def _wait_element_(self, by, value, delay=1):
        try:
            logger.info("Ожидаем на странице элемент")
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            element = self.driver.find_element(by, value)
            return element
        except (NoSuchElementException, TimeoutException):
            logger.info("Элемент на странице не найден")
            return False

    def _wait_element_to_clickable(self, by, value, delay=1):
        try:
            logger.info("Ожидаем, что элемент будет кликабилен")
            WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable((by, value)))
            element = self.driver.find_element(by, value)
            return element
        except (NoSuchElementException, TimeoutException):
            logger.info("Элемент на странице не найден")
            return False

    def _select_element(self, by, value, text):
        logger.info("Выбираем из списка: " + text)
        Select(self.driver.find_element(by, value)).select_by_visible_text(text)

    def _select_element_by_index(self, by, value, index=0):
        logger.info("Выбираем из списка элемент по индексу")
        list_el = self.driver.find_elements(by, value)
        list_el[index].click()

    def _select_len_list_element(self, by, value):
        logger.info("Узнаем длину списка")
        list_el = self.driver.find_elements(by, value)
        return len(list_el)

    def _input(self, by, value, text):
        logger.info("Находим элемент")
        element = self.driver.find_element(by, value)
        logger.info("Кликаем по элементу")
        element.click()
        logger.info("Очищаем значение")
        element.clear()
        logger.info("Вводим в поле: " + text)
        element.send_keys(text)

    def _get_element_text(self, selector, index):
        logger.info("Получаем элемент по индексу")
        return self.__element(selector, index).text
