import pytest
import requests


class APIClient:
    """
    Упрощенный клиент для работы с API
    Инициализируется базовым url на который пойдут запросы
    """
    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        return requests.post(url=url, params=params, data=data, headers=headers)

    def get(self, path="/", params=None):
        return requests.get(url=self.base_address + path, params=params)



def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="This is request url"
    )



@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)



@pytest.fixture
def fixture_api_response_ok(api_client):
    """Description: тест по домашнему заданию № 4   проверяем, что по url возвращается код 200"""
    res = api_client.get()
    if res.status_code == 200:
        result = True
    else:
        result = False
    return result
    # Проверяем что возвращаемые параметры верны
    assert result is True
