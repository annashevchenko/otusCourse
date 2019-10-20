from selenium.webdriver.common.by import By
from openCart.pages.BasePage import BasePage
from openCart.locators.CustomerLocators import CustomerLocations
from openCart.logging_openCart import logger


class CustomerPage(BasePage):

    # открываем раздел клиентов
    def open_customer(self):
        logger.info("Открываем Клиентов")
        self.driver.find_element(*CustomerLocations.CUSTOMER).click()

    # ожидаем отображение раздела в меню навигации
    def wait_section_in_menu_navigation(self, text):
        logger.info("Ожидаем отображение раздела " + text + " в меню навигации")
        self._wait_element_with_sleep(By.LINK_TEXT, text)

    # метод вводит в фильтре значение customer_name (имя клиента)
    def set_customer_name_in_filter(self, text_name):
        logger.info("Указываем product_name: " + text_name)
        self.driver.find_element(*CustomerLocations.NAME).send_keys(text_name)

    # ожидаем выпадающие меню
    def wait_menu(self):
        logger.info("Ожидаем выпадающее меню")
        self._wait_element_(By.CSS_SELECTOR, CustomerLocations.menu_search_context)

    # указываем email клиента
    def set_customer_email(self, text):
        logger.info("Указываем email клиента: " + text)
        self.driver.find_element(*CustomerLocations.EMAIL).send_keys(text)

    # метод выбирает в фильтре Customer Group (группа клиента)
    def set_customer_group_in_filter(self, text):
        logger.info("Выбираем группу клиента: " + text)
        self._select_element(By.ID, "input-customer-group", text)

    # метод выбирает в фильтре Status (статус клиента)
    def set_customer_status_in_filter(self, text):
        logger.info("Выбираем статус клиента: " + text)
        self._select_element(By.ID, "input-status", text)

    # указываем ip клиента
    def set_customer_ip(self, text):
        logger.info("Указываем ip клиента: " + text)
        self.driver.find_element(*CustomerLocations.IP).send_keys(text)

    # указываем Date Added клиента
    def set_customer_date_added(self, text):
        logger.info("Указываем дату создания клиента: " + text)
        self.driver.find_element(*CustomerLocations.DATEADDED).send_keys(text)

    # метод нажимает кнопку filter
    def button_filter(self):
        logger.info("Нажимает кнопку filter")
        self.driver.find_element(*CustomerLocations.FILTER).click()

    # находим отфильтрованное значение
    def find_filter_element(self, text):
        logger.info("Находим отфильтрованное значение")
        self.driver.find_element_by_xpath(CustomerLocations.customer_in_List.format(text))

    # указываем имя клиента для оплаты
    def set_customer_name_payment(self, text):
        logger.info("Указываем имя клиента для оплаты: " + text)
        self.driver.find_element(*CustomerLocations.NAME_PAYMENT).send_keys(text)

    # указываем фамилию клиента для оплаты
    def set_customer_lastname_payment(self, text):
        logger.info("Указываем фамилию клиента для оплаты: " + text)
        self.driver.find_element(*CustomerLocations.LASTNAME_PAYMENT).send_keys(text)

    # указываем адрес клиента для оплаты
    def set_customer_address_payment(self, text):
        logger.info("Указываем адрес клиента для оплаты: " + text)
        self.driver.find_element(*CustomerLocations.ADDRESS_PAYMENT).send_keys(text)

    # указываем город клиента для оплаты
    def set_customer_city_payment(self, text):
        logger.info("Указываем город клиента для оплаты: " + text)
        self.driver.find_element(*CustomerLocations.CITY_PAYMENT).send_keys(text)

    # указываем индекс клиента для оплаты
    def set_customer_postcode_payment(self, text):
        logger.info("Указываем индекс клиента для оплаты: " + text)
        self.driver.find_element(*CustomerLocations.POSTCODE_PAYMENT).send_keys(text)

    # метод выбирает Country (страна клиента)
    def select_customer_country_payment(self, text):
        logger.info("Выбираем страну клиента для оплаты: " + text)
        self._select_element(By.ID, "input-payment-country", text)

    # метод выбирает Region / State (регион клиента)
    def select_customer_region_payment(self, text):
        logger.info("Выбираем регион клиента для оплаты: " + text)
        self._select_element(By.ID, "input-payment-zone", text)

    # метод нажимает кнопку Continue
    def button_Continue_address(self):
        logger.info("Нажимает кнопку Continue")
        self.driver.find_element(*CustomerLocations.CONTINUE_ADDRESS).click()

    # метод нажимает кнопку Continue
    def button_сontinue_ship_address(self):
        logger.info("Нажимает кнопку Continue")
        self.driver.find_element(*CustomerLocations.CONTINUE_SHIP_ADDRESS).click()

    # метод нажимает кнопку Continue
    def button_Continue_ship_method(self):
        logger.info("Нажимает кнопку Continue")
        self.driver.find_element(*CustomerLocations.CONTINUE_SHIP_METHOD).click()

    # метод нажимает кнопку Continue
    def button_Continue_pay_method(self):
        logger.info("Нажимает кнопку Continue")
        self.driver.find_element(*CustomerLocations.CONTINUE_PAY_METHOD).click()

    # метод нажимает кнопку Confirm Order
    def button_Confirm_Order(self):
        logger.info("Нажимает кнопку Confirm Order")
        self.driver.find_element(*CustomerLocations.CONFIRM).click()

    # метод пишет комментарий к заказу при оплате
    def set_comment_customer_payment(self, text):
        logger.info("Пишем коимментарий к заказу при отплате: " + text)
        self.driver.find_element(*CustomerLocations.COMMENT).send_keys(text)

    # метод нажимает checkbox_agree
    def checkbox_agree(self):
        logger.info("Нажимаем checkbox_agree")
        self.driver.find_element_by_css_selector(CustomerLocations.checkbox_agree).click()

    def checked_shipping_address(self):
        logger.info("находим подтвердение указанного адреса доставки")
        self._wait_element_(By.CSS_SELECTOR, CustomerLocations.checked_shipping_address)
        # self.driver.find_element_by_css_selector(CustomerLocations.checked_shipping_address)
