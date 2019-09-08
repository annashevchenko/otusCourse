""""описание элементов загрузки файлов под админом в OpenCart"""


class DownLoadLocators:
    '''поиск кнопки добавить новую загрузку'''
    button_add_new_download = "a[data-original-title='Add New']"

    '''поиск кнопки добавить новую загрузку'''
    button_delete_download = "button[type='button']"

    '''поиск поля для указания наименование загрузки'''
    download_name = "input[name='download_description[1][name]']"

    '''поиск поля для указания наименование файла'''
    file_name = "input[name='filename']"

    '''поиск поля для указания наименование маски'''
    mask_name = "input[name='mask']"

    '''поиск кнопки button-upload'''
    button_upload = "button[id='button-upload']"

    '''поиск кнопки отменить загрузку'''
    button_cancel_download = "a[data-original-title='Cancel']"

    '''поиск кнопки сохранить загрузку'''
    button_save_download = "button[data-original-title='Save']"

    '''поиск поля для указания загружаемого файла файла'''
    file = "input[name='file']"

    '''поиск наименование загруженного файла'''
    find_name_download = "*//td[@class='text-left'][text()='{0}']"