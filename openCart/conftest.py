import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from openCart.logging_openCart import logger


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default='chrome',
        help="This is Browser name"
    )
    parser.addoption(
        "--url",
        action="store",
        default="http://localhost/",
        help="This is request url"
    )
    parser.addoption(
        "--wait",
        action="store",
        default="10",
        help="This is request url"
    )


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    wd = None
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--start-maximized')
        options.add_experimental_option('w3c', False)
        caps = DesiredCapabilities.CHROME
        caps['loggingPrefs'] = {'browser': 'INFO'}
        wd = EventFiringWebDriver(webdriver.Chrome(desired_capabilities=caps, options=options), MyListener())
        wd.implicitly_wait(request.config.getoption("--wait"))
        wd.get(request.config.getoption("--url"))
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--start-maximized')
        options.add_experimental_option('w3c', False)
        caps = DesiredCapabilities.FIREFOX
        caps['loggingPrefs'] = {'browser': 'INFO'}
        wd = EventFiringWebDriver(webdriver.Firefox(desired_capabilities=caps, options=options), MyListener())
        wd.implicitly_wait(request.config.getoption("--wait"))
        wd.get(request.config.getoption("--url"))
    elif browser == 'ie':
        options = webdriver.IeOptions()
        # options.add_argument('--headless')
        options.add_argument('window-size=1920x935')
        wd = webdriver.IeOptions(options=options)
        wd.implicitly_wait(request.config.getoption("--wait"))
        wd.get(request.config.getoption("--url"))
    else:
        print('Unsupported browser!')
    yield wd
    request.addfinalizer(wd.close)

class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        logger.info(msg="ищем элемент: " + value)

    def after_find(self, by, value, driver):
        logger.info(msg="найден элемент: " + value)

    def after_click(self, element, driver):
        logger.info(msg="кликнули по элементу: ")

    def after_change_value_of(self, element, driver):
        logger.info(msg="изменили значение элемента")

    def on_exception(self, exception, driver):
        screen_file_name = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S") + '_screenshort.png'
        driver.save_screenshot("/home/anna/PycharmProjects/homework/openCart/screenshorts/" + screen_file_name)
