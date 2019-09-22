import allure
from selenium.webdriver.common.by import By
from openCart.pages.BasePage import BasePage
from openCart.locators.CatalogProductLocators import CatalogProductLocators
from openCart.logging_openCart import logger


class CatalogPage(BasePage):

    # открываем каталог
    def open_catalog(self):
        logger.info("Открываем Каталог")
        with allure.step("Открываем Каталог"):
            self.driver.find_element(*CatalogProductLocators.CATALOG).click()

    # ожидаем отображение раздела в меню навигации
    def wait_section_in_menu_navigation(self, text):
        logger.info("Ожидаем отображение раздела " + text + " в меню навигации")
        with allure.step("Ожидаем отображение раздела " + text + " в меню навигации"):
            self._wait_element_with_sleep(By.LINK_TEXT, text)

    # нажимаем кнопку добавить новый продукт
    def button_add_new_product(self):
        logger.info("нажимаем кнопку добавить новый продукт")
        with allure.step("нажимаем кнопку добавить новый продукт"):
            self.driver.find_element_by_css_selector(CatalogProductLocators.button_add_new).click()

    # указываем наименование продукта
    def set_product_name(self, text):
        logger.info("Указываем наименование продукта: " + text)
        with allure.step("Указываем наименование продукта: " + text):
            self.driver.find_element(*CatalogProductLocators.NAMEPRODUCT).send_keys(text)

    # указываем описание продукта
    def set_product_description(self, text):
        logger.info("Указываем описание продукта: " + text)
        with allure.step("Указываем описание продукта: " + text):
            self.driver.find_element_by_css_selector(CatalogProductLocators.description_product).send_keys(text)

    # указываем наименование продукта
    def set_product_meta_tag(self, text):
        logger.info("Указываем наименование продукта: " + text)
        with allure.step("Указываем наименование продукта: " + text):
            self.driver.find_element(*CatalogProductLocators.METATEG).send_keys(text)

    # указываем модель продукта
    def set_product_model(self, text):
        logger.info("Указываем модель продукта: " + text)
        with allure.step("Указываем модель продукта: " + text):
            self.driver.find_element(*CatalogProductLocators.MODEL).send_keys(text)

    # сохраняем продукт
    def save_product(self):
        logger.info("Выполняем сохранение")
        with allure.step("Выполняем сохранение"):
            self.driver.find_element_by_css_selector(CatalogProductLocators.button_save_new_product).click()

    # метод вводит в фильтре значение product_name (наименование)
    def set_product_name_in_filter(self, text_product_name):
        logger.info("Указываем product_name: " + text_product_name)
        with allure.step("Указываем product_name: " + text_product_name):
            self.driver.find_element(*CatalogProductLocators.NAME).send_keys(text_product_name)

    # ожидаем сообщение
    def wait_menu(self):
        logger.info("Ожидаем сообщение")
        with allure.step("Ожидаем сообщение"):
            self._wait_element_(By.CSS_SELECTOR, CatalogProductLocators.menu_search_context)

    # метод вводит в фильтре значение price (стоимость)
    def set_product_price_in_filter(self, text_price):
        logger.info("Указываем price: " + text_price)
        with allure.step("Указываем price: " + text_price):
            self.driver.find_element(*CatalogProductLocators.PRICE).send_keys(text_price)

    # метод вводит в фильтре значение product_quantity (количество)
    def set_product_quantity_in_filter(self, text):
        logger.info("Указываем product_quantity: " + text)
        with allure.step("Указываем product_quantity: " + text):
            self.driver.find_element(*CatalogProductLocators.QUANTITY).send_keys(text)

    # метод выбирает в фильтре значение status (статус)
    def set_product_status_in_filter(self, text):
        logger.info("Выбираем status: " + text)
        with allure.step("Выбираем status: " + text):
            self._select_element(By.ID, "input-status", text)

    # метод нажимает кнопку filter
    def button_filter(self):
        logger.info("Нажимает кнопку filter")
        with allure.step("Нажимает кнопку filter"):
            self.driver.find_element(*CatalogProductLocators.FILTER).click()

    # находим отфильтрованное значение
    def find_filter_element(self, text):
        logger.info("Находим отфильтрованное значение")
        with allure.step("Находим отфильтрованное значение"):
            self.driver.find_element_by_xpath(CatalogProductLocators.product_in_productList.format(text))

    # находим и записываем в список все checkbox в списке, устанавливаем первый
    def set_checkbox_in_product_list(self):
        logger.info("Находим и записываем в список все checkbox в списке, устанавливаем первый из них")
        with allure.step("Находим и записываем в список все checkbox в списке, устанавливаем первый из них"):
            self._select_element_by_index(By.CSS_SELECTOR, CatalogProductLocators.checkbox_in_productList)

    # метод нажимает кнопку удалить продукт
    def button_delete(self):
        logger.info("Нажимает кнопку удалить")
        with allure.step("Нажимает кнопку удалить"):
            self.driver.find_element_by_css_selector(CatalogProductLocators.button_delete_product).click()

    # находим и записываем в список все кнопки Edit в списке, нажимаем на первую кнопку
    def set_buttons_edit_in_product_list(self):
        logger.info("Находим и записываем в список все кнопки Edit в списке, нажимаем на первую кнопку")
        with allure.step("Находим и записываем в список все кнопки Edit в списке, нажимаем на первую кнопку"):
            self._select_element_by_index(By.CSS_SELECTOR, CatalogProductLocators.buttons_edit_in_productList)

    # метод вводит значение price в разделе Date
    def set_product_price(self, text):
        logger.info("Вводим значение price: " + text + " в разделе Date")
        with allure.step("Вводим значение price: " + text + " в разделе Date"):
            self._input(*CatalogProductLocators.PRICE, text)

    # метод нажимает кнопку копировать продукт
    def button_copy(self):
        logger.info("Нажимает кнопку копировать продукт")
        with allure.step("Нажимает кнопку копировать продукт"):
            self.driver.find_element_by_css_selector(CatalogProductLocators.button_copy_product).click()

    # находим длину списка
    def len_product_list(self):
        logger.info("Находим длину списка")
        with allure.step("Находим длину списка"):
            list_len = self._select_len_list_element(By.CSS_SELECTOR, CatalogProductLocators.checkbox_in_productList)
        return list_len

    # находим и записываем в список все checkbox в списке, устанавливаем последний
    def set_last_checkbox_in_product_list(self):
        logger.info("Находим и записываем в список все checkbox в списке, устанавливаем последний")
        with allure.step("Находим и записываем в список все checkbox в списке, устанавливаем последний"):
            self._select_element_by_index(By.CSS_SELECTOR, CatalogProductLocators.checkbox_in_productList, -1)

    # переходи на страницу
    def open_page(self, text):
        logger.info("Переходим на страницу: " + text)
        with allure.step("Переходим на страницу: " + text):
            self.driver.find_element_by_xpath(CatalogProductLocators.pagination_in_productList.format(text)).click()

    # проверяем активную страницу
    def active_page(self, text):
        logger.info("Проверяем, что страница: " + text + " активна")
        with allure.step("Проверяем, что страница: " + text + " активна"):
            self.driver.find_element_by_xpath(CatalogProductLocators.active_page.format(text))

    # нажимаем кнопку image
    def set_product_image(self):
        logger.info("Нажимаем кнопку image")
        with allure.step("Нажимаем кнопку image"):
            self.driver.find_element(*CatalogProductLocators.IMAGE).click()
            self._wait_element_(By.CSS_SELECTOR, CatalogProductLocators.modal_image)

    # выбираем изображение image
    def select_product_image(self, text_image):
        logger.info("Выбираем изображение: " + text_image)
        with allure.step("Выбираем изображение: " + text_image):
            self.driver.find_element_by_css_selector(CatalogProductLocators.directory).click()
            self._wait_element_to_clickable(By.CSS_SELECTOR, CatalogProductLocators.image.format(text_image))
            self.driver.find_element_by_css_selector(CatalogProductLocators.image.format(text_image)).click()
