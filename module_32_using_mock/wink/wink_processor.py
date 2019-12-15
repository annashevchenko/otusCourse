import requests
import json

from module_32_using_mock.wink.payload_utils import get_session

LIST_MOVIES_URL = 'https://cnt-odcv-itv02.svc.iptv.rt.ru/api/v2/portal/media_views/28?offset=4'


def make_depersonalized_session():
    response = requests.post('https://cnt-odcv-itv02.svc.iptv.rt.ru/api/v2/portal/session_tokens')
    if response.status_code != 200:
        raise Exception
    session = get_session(response.content)
    return session


def get_kids_result():
    session = make_depersonalized_session()
    response = requests.get(LIST_MOVIES_URL,
                            headers={'session_id': session.session_id})
    media_data = json.loads(response.content.decode("utf-8"))
    return media_data


print(get_kids_result())
