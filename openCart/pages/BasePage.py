import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def _wait_element_with_sleep(self, by, selector, num_count=10, num_sleep=1):
        count = 0
        while count < num_count:
            try:
                self.driver.find_element(by, selector)
                break
            except NoSuchElementException:
                count += 1
                time.sleep(num_sleep)

    def _wait_element_(self, by, value, delay=1):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            element = self.driver.find_element(by, value)
            return element
        except (NoSuchElementException, TimeoutException):
            return False

    def _wait_element_to_clickable(self, by, value, delay=1):
        try:
            WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable((by, value)))
            element = self.driver.find_element(by, value)
            return element
        except (NoSuchElementException, TimeoutException):
            return False

    def _select_element(self, by, value, text):
        Select(self.driver.find_element(by, value)).select_by_visible_text(text)

    def _select_element_by_index(self, by, value, index=0):
        list_el = self.driver.find_elements(by, value)
        list_el[index].click()

    def _select_len_list_element(self, by, value):
        list_el = self.driver.find_elements(by, value)
        return len(list_el)

    def _input(self, by, value, text):
        element = self.driver.find_element(by, value)
        element.click()
        element.clear()
        element.send_keys(text)

    def _get_element_text(self, selector, index):
        return self.__element(selector, index).text
