from selenium.webdriver.common.by import By

"""описание элементов раздела клиентов в OpenCart"""


class CustomerLocations:
    '''находим раздел Customers в меню'''
    CUSTOMER = (By.ID, "menu-customer")

    '''находим подраздел Customers в меню'''
    customers = ("*//li[@id='menu-customer']//a[text()='Customers']")

    '''поля для ввода имя клиента'''
    NAME = (By.ID, "input-name")

    '''поля для ввода email клиента'''
    EMAIL = (By.ID, "input-email")

    '''поля для ввода ip клиента'''
    IP = (By.ID, "input-ip")

    '''поля для ввода date-added клиента'''
    DATEADDED = (By.ID, "input-date-added")

    '''кнопка filter'''
    FILTER = (By.ID, "button-filter")

    '''поиск меню контекстного поиска в фильтре'''
    menu_search_context = "ul[style='top: 133px; left: 31px; display: block;']"

    '''поиск в Customer по тексту'''
    customer_in_List = "*//tbody//td[text()='{0}']"
