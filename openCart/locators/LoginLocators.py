"""описание элементов авторизации и регистрации в OpenCart"""


class LoginLocators:
    '''поиск элемента панели управления данными пользователя'''
    top_element = "a[title='{0}']"

    '''поиск radioButton подписки при регистрации нового пользователя'''
    subscribe = "input[name='newsletter'][value='{0}']"

    '''проверка на открытие раздела '''
    message_in_header = "*//div[@id='content']//h1[text()='{0}']"

    '''поиск кнопки Продолжить после создания аккаунта'''
    сontinue_account_created = "div[class='buttons'] a"

    '''проверка на открытие раздела '''
    header_in_account = "*//div[@id='content']//h2[text()='{0}']"

    '''поиск кнопки login на входе под админом '''
    button_login = "button[class = 'btn btn-primary']"

    '''поиск кнопки login на входе под пользователем '''
    button_user_login = "input[value = 'Login']"
