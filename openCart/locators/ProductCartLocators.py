"""описание элементов карточки продукта в OpenCart"""


class PProductCartLocators:
    '''поиск карточки товара по названию'''
    image_in_cart_by_name = "div[class='product-thumb'] a img[title='{0}']"

    '''поиск карточки товара по названию'''
    header_cart_by_name = "*//div[@id='content']//h1[text()='{0}']"

    '''поиск наименований характеристик продукта'''
    info_in_cart_product = "*//ul[@class='list-unstyled']//li[text()='{0}']"

    '''поиск кнопки добавить продукт в Wish List'''
    button_WishList = "div[class='btn-group'] button[data-original-title='Add to Wish List']"

    '''поиск кнопки добавить новый продукт Add_new в Product List'''
    button_Add_New = "a[data-original-title = 'Add New']"
