def test_search_by_text(browser_grid):
    """Тест находит поле поиска, вводит в поле данны для поиска, нажимает кнопку найти. Находит заголовок результат поиска"""
    find_text = "mac"
    element = browser_grid.find_element_by_css_selector("input[name='search']")
    element.click()
    element.send_keys(find_text)
    browser_grid.find_element_by_css_selector("div[id = 'search'] button").click()
    browser_grid.find_element_by_xpath("*//h1[text()='Search - " + find_text + "']")