import pytest

from selenium import webdriver


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


@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("--browser")
    wd = None
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--start-maximized')
        wd = webdriver.Chrome(options=options)
        wd.get(request.config.getoption("--url"))
    if browser == 'firefox':
        options = webdriver.FirefoxOptions()
        # options.add_argument('--headless')
        options.add_argument('--start-maximized')
        wd = webdriver.Firefox(options=options)
        wd.get(request.config.getoption("--url"))
    if browser == 'ie':
        options = webdriver.IeOptions()
        # options.add_argument('--headless')
        options.add_argument('window-size=1920x935')
        options = webdriver.IeOptions(options=options)
        browser.get(request.config.getoption("--url"))
    else:
        print('Unsupported browser!')
    yield wd
    if wd is not None:
        wd.close()
