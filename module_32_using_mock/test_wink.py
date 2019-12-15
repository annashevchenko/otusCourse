import pytest
import requests_mock

from module_32_using_mock.wink.payload_utils import Session
from module_32_using_mock.wink.wink_processor import LIST_MOVIES_URL
from module_32_using_mock.wink.wink_processor import get_kids_result
from unittest.mock import patch


def test_get_media_items():
    kids = get_kids_result()
    assertions(kids)


@pytest.fixture
def mock():
    with requests_mock.Mocker() as mock_instance:
        yield mock_instance


def mocked_session():
    yield Session('TEST_SESSION_ID', 'UNAUTHORIZED')


def test_get_media_items_mocked(mock):
    with patch('module_32_using_mock.wink.wink_processor.make_depersonalized_session', side_effect=mocked_session()):
        mock.get(LIST_MOVIES_URL, text='{"id": 28, "name": "Детям", "alias": "kids",'
                                       '"media_blocks":[{"name": "BabyTV"}, {"name": "Анимация Pixar"},'
                                       '{"name": "Классика Disney"},{"name": "Популярные мультсериалы"},'
                                       '{"name": "Популярные мультфильмы"}, {"name": "Союзмультфильм"}]}')
        kids = get_kids_result()
        assertions(kids)


def assertions(kids):
    assert kids['name'] == 'Детям'
    assert kids['alias'] == 'kids'
    name_block = set()
    name_block_const = {'BabyTV', 'Анимация Pixar', 'Классика Disney', 'Популярные мультсериалы',
                        'Популярные мультфильмы', 'Союзмультфильм'}
    for media_block in kids['media_blocks']:
        name_block.add(media_block['name'])
    assert name_block == name_block_const
