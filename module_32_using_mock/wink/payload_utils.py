import json


class Session(object):
    def __init__(self, session_id, session_state):
        self.session_id = session_id
        self.session_state = session_state


def session_decoder(obj):
    return Session(obj['session_id'], obj['session_state'])


def get_session(data):
    return json.loads(data, object_hook=session_decoder)
