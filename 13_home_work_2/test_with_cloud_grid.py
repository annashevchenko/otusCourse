from openCart.locators import LoginLocators, CustomerLocations
from openCart.pages import CustomerPage


def test_google(driver):
    driver.get("http://www.google.com/ncr")
    if not "Google" in driver.title:
        raise Exception("Unable to load google page!")
    elem = driver.find_element_by_name("q")
    elem.send_keys("BrowserStack")
    elem.submit()
    print(driver.title)


def test_filter_customer(driver):
    """Тест выполняет открывает раздел Customers"""
    # открываем раздел клиентов и заходим в Customers
    driver.get("https://demo.opencart.com/admin")
    driver.find_element_by_css_selector(LoginLocators.button_login).click()
    CustomerPage(driver).open_customer()
    CustomerPage(driver).wait_section_in_menu_navigation("Customers")
    driver.find_element_by_xpath(CustomerLocations.customers).click()