from selenium.webdriver.common.action_chains import ActionChains


def test_use_drag_and_drop(driver):
    """Тест использует инструмент drag_and_drop для переноса в корзину элементов"""
    # находим корзину, в которую будут перенесены элементы
    element_trash = driver.find_element_by_css_selector("div[class='trash']")
    # выполняем цикл для каждого найденного элемента выполняем перенос в корзину через drag_and_drop
    # и проверяем, что корзина полная после каждого переноса
    for element in driver.find_elements_by_css_selector("div[class='container'] img"):
        ActionChains(driver).drag_and_drop(element, element_trash).perform()
        driver.find_element_by_css_selector("div[class='trash full']")
