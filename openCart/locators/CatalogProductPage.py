"""описание элементов карточки продукта в OpenCart"""


class CatalogProductPage:
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
