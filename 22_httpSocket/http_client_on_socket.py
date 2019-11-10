import argparse
import socket
import ssl


def get_headers_str(headers) -> str:
    # получить строку заголовков
    s = ''
    for k, v in headers:
        s += k + ': ' + v + '\n'
    return s


def get_data_from_socket(sock):
    result = b''
    while True:
        block = sock.recv(4096)
        result += block
        if (block.find(b'</html>') != -1) or (block.find(b'</HTML>') != -1):
            break
    return result


def get_response_status(data):
    splitted = data.split(b' ')
    return splitted[0], int(splitted[1]), splitted[2]


def get_headers_block(data):
    data = data.decode("utf-8")
    headers = {}
    splitted = data.split('\r\n')
    for header in splitted:
        pos = header.find(':')
        k = header[:pos].strip()
        v = header[pos + 1:].strip()
        headers[k] = v
    return headers


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Params to receive resource by HTTP')
    parser.add_argument('-m', '--method', action='store', default='GET')
    parser.add_argument('-r', '--resource', action='store', default='')
    parser.add_argument('-s', '--host', action='store', help='host should be specified', required=True)
    parser.add_argument('-p', '--port', action='store', default=443)
    parser.add_argument('-hr', '--headers', action='store', nargs='+', default=[])
    arg = parser.parse_args()

    headers = []
    for header in arg.headers:
        val = header.split(':')
        headers.append((val[0], val[1]))

    arg.headers = headers

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    context.load_default_certs()

    server_ip = socket.gethostbyname(arg.host)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock = context.wrap_socket(sock, server_hostname=arg.host)

    request_template = "{method} /{resource} HTTP/1.1\n" \
                       "Host: {host}\n" + \
                       "{headers}" + \
                       "\n"
    request = request_template.format(
        method=arg.method,
        resource=arg.resource,
        host=arg.host,
        headers=get_headers_str(arg.headers)
    )

    sock.connect((arg.host, arg.port))
    sock.send(request.encode())
    data = get_data_from_socket(sock)

    # получим первую строку со статусом ответа
    pos = data.find(b'\r\n')
    response_status = get_response_status(data[:pos])
    data = data[pos + 2:]

    # получим блок заголовков
    pos = data.find(b'\r\n\r\n')
    response_headers = get_headers_block(data[:pos])
    data = data[pos + 4:]

    # получим контент запроса
    response_content = data

    print('Response code: ', response_status[1])
    print('Response headers: ', response_headers)
    print('Response content: ', response_content)
    pass
