from selenium.webdriver.common.by import By

"""описание элементов карточки продукта в OpenCart"""


class CatalogProductLocators:
    '''находим раздел Catalog в меню'''
    CATALOG = (By.ID, "menu-catalog")


    '''поля для ввода наименования продукта'''
    NAMEPRODUCT = (By.ID, "input-name1")

    '''поля для ввода meta_tag'''
    METATEG = (By.ID, "input-meta-title1")

    '''поля для ввода model'''
    MODEL = (By.ID, "input-model")

    '''поля для ввода model'''
    NAME = (By.ID, "input-name")

    '''поля для ввода price'''
    PRICE = (By.ID, "input-price")

    '''поля для ввода quantity'''
    QUANTITY = (By.ID, "input-quantity")

    '''поля для ввода status'''
    STATUS = (By.ID, "input-status")

    '''кнопка filter'''
    FILTER = (By.ID, "button-filter")

    '''кнопка image'''
    IMAGE = (By.ID, "button-image")

    '''поиск кнопки добавить новый продукт Add_new в Product List'''
    button_add_new = "a[data-original-title = 'Add New']"

    '''поиск кнопки сохранить новый продукт Add_new в Product List'''
    button_save_new_product = "button[data-original-title = 'Save']"

    '''поиск кнопки удалить продукт в Product List'''
    button_delete_product = "button[data-original-title = 'Delete']"

    '''поиск кнопки копировать продукт в Product List'''
    button_copy_product = "button[data-original-title = 'Copy']"

    '''поиск поля Описание description в Product List'''
    description_product = "div[class = 'note-editable panel-body']"

    '''поиск сообщения после успешных действий  над продуктом продукта'''
    mess_by_product = "div[class='alert alert-success alert-dismissible']"

    '''поиск кнопки закрыть сообщение'''
    button_close_mess = "button[class='close']"

    '''поиск меню контекстного поиска в фильтре'''
    menu_search_context = "ul[style='top: 133px; left: 31px; display: block;']"

    '''поиск в Product List по тексту'''
    product_in_productList = "*//tbody//td[text()='{0}']"

    '''поиск в Product List checkBox у продуктов'''
    checkbox_in_productList = "tbody td input[type='checkbox']"

    '''поиск в Product List кнопки Редактировать у продуктов'''
    buttons_edit_in_productList = "tbody tr td a[data-original-title='Edit']"

    '''поиск в Product List наименование продуктов'''
    img_in_productList = "tbody tr img"

    '''поиск в Product List наименование продуктов'''
    pagination_in_productList = "*//ul[@class='pagination']//li//a[text()='{0}']"

    '''поиск в Product List наименование продуктов'''
    active_page = "*//ul[@class='pagination']//li[@class='active']//span[text()='{0}']"

    '''поиск в формы для добавления изображения'''
    modal_image = "div[id='modal-image'][style='display: block;']"

    '''поиск директории'''
    directory = "a[class='directory']"

    '''поиск  изображения'''
    image = "a img[title='{0}']"