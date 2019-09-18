"""описание элементов главной страницы OpenCart"""
from selenium.webdriver.common.by import By


class MainLocators:
    '''поле поиска'''
    search = "input[name='search']"

    '''кнопка найти'''
    search_button = "div[id = 'search'] button"

    '''проверка на открытие меню Desktops'''
    open_menu = "*//a[@aria-expanded='true'][text()='{0}']"

    '''проверка на открытие раздела '''
    search_result = "*//h1[text()='Search - {0}']"

    '''находим корзину'''
    CART = (By.ID, "cart")

    '''сообщение о пустой корзине'''
    cart_text = "*//div[@id='cart']//p[text()='{0}']"

    '''сообщение о пустой корзине'''
    directory = "*//a[text()='{0}']"

    '''поиск сообщения после успешных действий  над продуктом продукта'''
    mess = "div[class='alert alert-success alert-dismissible']"

    '''поиск Shopping Cart'''
    shopping_cart = "a[title='Shopping Cart']"

    '''находим заголовок'''
    heading = "*//h1[text()='{0}']"
