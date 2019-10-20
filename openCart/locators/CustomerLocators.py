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

    '''поля для ввода имя клиента'''
    NAME_PAYMENT = (By.ID, "input-payment-firstname")

    '''поля для ввода фамилии клиента'''
    LASTNAME_PAYMENT = (By.ID, "input-payment-lastname")

    '''поля для ввода адреса клиента'''
    ADDRESS_PAYMENT = (By.ID, "input-payment-address-1")

    '''поля для ввода города клиента'''
    CITY_PAYMENT = (By.ID, "input-payment-city")

    '''поля для ввода индекса клиента'''
    POSTCODE_PAYMENT = (By.ID, "input-payment-postcode")

    '''кнопка продолжить'''
    CONTINUE_ADDRESS = (By.ID, "button-payment-address")

    '''кнопка продолжить'''
    CONTINUE_SHIP_ADDRESS = (By.ID, "button-shipping-address")

    '''кнопка продолжить'''
    CONTINUE_SHIP_METHOD = (By.ID, "button-shipping-method")

    '''кнопка продолжить'''
    CONTINUE_PAY_METHOD = (By.ID, "button-payment-method")

    '''кнопка продолжить'''
    CONFIRM = (By.ID, "button-confirm")

    '''поле для ввода комментария'''
    COMMENT = (By.NAME, "comment")

    '''Terms & Conditions'''
    checkbox_agree = "input[type='checkbox'][name='agree']"

    '''checked shipping_address'''
    checked_shipping_address = "input[name='shipping_address'][checked='checked']"
