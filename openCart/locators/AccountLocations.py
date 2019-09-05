from selenium.webdriver.common.by import By

"""описание элементов для работы с аккунтом"""


class AccountLocations:
    '''находим раздел My Account'''
    my_account_link = "a[title='My Account']"

    '''находим выпадающее меню My Account'''
    my_account_menu = "li[class='dropdown open'] a[title='My Account'][aria-expanded='true']"

    '''находим в выпадающем меню My Account Register'''
    my_account_Register = "*//a[text()='Register']"

    '''находим в выпадающем меню My Account Login'''
    my_account_Login = "*//a[text()='Login']"

    '''находим регистрационные поля Register Account'''
    FIRSTNAME = (By.ID, "input-firstname")
    LASTNAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    PHONE = (By.ID, "input-telephone")
    PASSWORD = (By.ID, "input-password")
    COMFIRMPASS = (By.ID, "input-confirm")

    '''поиск radioButton подписки при регистрации нового пользователя'''
    subscribe = "input[name='newsletter'][value='{0}']"

    POLITICPRIVACY = (By.NAME, "agree")

    '''поиск кнопки Продолжить при создании нового пользователя'''
    CONTINUE = (By.CSS_SELECTOR, "input[value='Continue']")

    '''проверка на открытие раздела '''
    message_in_header = "*//div[@id='content']//h1[text()='{0}']"

    '''поиск кнопки Продолжить после создания аккаунта'''
    сontinue_account_created = "div[class='buttons'] a"

    '''проверка на открытие раздела '''
    header_in_account = "*//div[@id='content']//h2[text()='{0}']"

    '''открытие раздела '''
    section = "*//a[text()='{0}']"

