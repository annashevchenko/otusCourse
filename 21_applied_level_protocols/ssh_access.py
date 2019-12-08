import http.client
import re
from time import sleep


def test_ssh_access(ssh_client):
    """Проверяем  access.log сервера apache и убеждаемся,
    что обращения к opencart действительно отражаются в логе на сервере"""

    # просто отправим тестовую команду
    assert exec_command(ssh_client, 'pwd').strip() == '/home/bitnami'
    # запрос заглавную страницу
    check_resource_request(ssh_client, '/', 200)
    check_resource_request(ssh_client, '/index.php?route=product/category&path=57', 200)
    pass


def check_resource_request(ssh_client, uri, code):
    """Метод обращается к opencart как клиент и затем проверяет лог на сервере"""
    # установим соединение с opencart как клиент
    conn = http.client.HTTPConnection('localhost', 80)
    request_url(conn, uri)
    # небольшая задрежка, что бы изменения успели попасть в лог
    sleep(0.05)
    # проверим лог
    log_str = get_last_access_log_line(ssh_client)
    log_data = get_log_data(log_str)
    assert log_data['uri'] == uri
    assert log_data['code'] == code


def get_log_data(log_str):
    """Получить информацию из последней строчки лога"""
    pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.*\[.*\]\s\"GET\s(.*)\sHTTP/1\.1\"\s(\d*)\s(\d*)')
    search = pattern.search(log_str)
    log_data = {
        'uri': search.group(1),
        'code': int(search.group(2)),
        'size': int(search.group(3))
    }
    return log_data


def get_last_access_log_line(ssh_client):
    last_log = exec_command(ssh_client, 'tail /opt/bitnami/apache/logs/access_log')
    last_line = last_log.strip().split('\n')[-1]
    return last_line


def request_url(conn, url):
    conn.request("GET", url)
    resp = conn.getresponse()
    assert resp.status == 200


def exec_command(client, cmd: str) -> str:
    """Выполняет команду на ssh-сервере"""
    stdin, stdout, stderr = client.exec_command(cmd)
    data = stdout.read() + stderr.read()
    return data.decode('utf-8')
