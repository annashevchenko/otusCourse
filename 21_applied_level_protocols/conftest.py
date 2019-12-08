import paramiko
import pytest


@pytest.fixture(scope="session")
def config():
    """Конфигурация для доступа к SSH-серверу.
    Сервер SSH должен быть предварительно настроен и запущен."""
    config = {
        'ssh_host': 'localhost',
        'ssh_user': 'bitnami',
        'ssh_password': 'bitnami',
        'ssh_port': 1022
    }
    yield config


@pytest.fixture(scope="session")
def ssh_client(request, config):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=config['ssh_host'], username=config['ssh_user'],
                   port=config['ssh_port'], password=config['ssh_password'])
    yield client
    client.close()
