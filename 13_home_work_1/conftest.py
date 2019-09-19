import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

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


@pytest.fixture()
def browser_grid(request):
    browser = request.config.getoption("--browser")
    wd = None
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        caps = DesiredCapabilities.CHROME
        wd = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                              desired_capabilities=caps, options=options)
        wd.get(request.config.getoption("--url"))
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--start-maximized')
        caps = DesiredCapabilities.FIREFOX
        wd = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                               desired_capabilities=caps, options=options)
        wd.get(request.config.getoption("--url"))
    else:
        print('Unsupported browser!')
    yield wd
    request.addfinalizer(wd.close)
