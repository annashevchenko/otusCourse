import pytest


def test_api_response_ok(api_client):
    """Description: тест по домашнему заданию № 4   проверяем, что по url возвращается код 200"""
    res = api_client.get()
    # Проверяем что возвращаемые параметры верны
    assert res.status_code == 200