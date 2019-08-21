"""описание элементов авторизации и регистрации в OpenCart"""


class LoginPage:
    '''поиск элемента панели управления данными пользователя'''
    top_element = "a[title='{0}']"

    '''поиск radioButton подписки при регистрации нового пользователя'''
    subscribe = "input[name='newsletter'][value='{0}']"


    '''поиск кнопки Продолжить при создании нового пользователя'''
    сontinue = "input[value='Continue']"


    '''проверка на открытие раздела '''
    message_in_header = "*//div[@id='content']//h1[text()='{0}']"



    '''поиск кнопки Продолжить после создания аккаунта'''
    сontinue_account_created = "div[class='buttons'] a"

    '''проверка на открытие раздела '''
    header_in_account = "*//div[@id='content']//h2[text()='{0}']"