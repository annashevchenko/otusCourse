"""описание элементов главной страницы OpenCart"""


class MainLocators:
    '''поле поиска'''
    seach = "input[name='search']"

    '''кнопка найти'''
    seach_button = "div[id = 'search'] button"

    '''проверка на открытие меню Desktops'''
    open_menu = "*//a[@aria-expanded='true'][text()='{0}']"

    '''проверка на открытие раздела '''
    menu_mac = "*//div[@id='content']//h2[text()='{0}']"


