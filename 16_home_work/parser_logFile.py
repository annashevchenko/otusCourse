import argparse
import json
import re
import typing

LogLineInfo = typing.NamedTuple('LogLineInfo', [('ip', str),
                                                ('method', str),
                                                ('resource', str),
                                                ('code', int),
                                                ('bytes_cnt', int),
                                                ('from_address', str),
                                                ('user_agent', str),
                                                ('time_ms', int)])


def make_errs_dict(spec_line, count):
    (method, url, status, ip) = spec_line.split('#')
    return {'method': method, 'url': url, 'status': status, 'ip': ip, 'count': count}


def process(filename: str):
    # общее число валидных запросов
    total = 0
    # число запросов по методам
    call_by_methods = {'GET': 0, 'HEAD': 0, 'POST': 0, 'PUT': 0, 'DELETE': 0, 'PATCH': 0}
    # список ip адресов
    ip_address = {}
    # запросы по времени
    req_by_time = {}
    # клиентские и серверные ошибки
    client_errs = {}
    server_errs = {}
    with open(filename, "r") as file:
        for line in file:
            log_line_info = create_info(line)
            if log_line_info is None:
                continue
            # инкремент по числу запросов
            total += 1
            # инкремент по типу метода
            call_by_methods[log_line_info.method] += 1
            # счетчик по ip адресам
            if ip_address.get(log_line_info.ip) is None:
                ip_address[log_line_info.ip] = 0
            ip_address[log_line_info.ip] += 1
            # записываем информацию по времени запроса
            req_by_time[log_line_info.time_ms] = {'method': log_line_info.method,
                                                  'url': log_line_info.resource,
                                                  'ip': log_line_info.ip,
                                                  'time': log_line_info.time_ms}
            # сохраняем информацию по клиентским ошибкам и серверным ошибкам
            code = log_line_info.code // 100
            if code == 4 or code == 5:
                key = log_line_info.method + '#' + log_line_info.resource + '#' \
                      + str(log_line_info.code) + '#' + str(log_line_info.ip)
                if code == 4:
                    errs = client_errs
                else:
                    errs = server_errs
                if errs.get(key) is None:
                    errs[key] = 0
                errs[key] += 1

    # вычисляем топ 10 ip адресов
    ip_address_sorted = [(k, ip_address[k]) for k in sorted(ip_address, key=ip_address.get, reverse=True)][:10]
    ip_address_top = {k: v for (k, v) in ip_address_sorted}
    # вычисляем топ 10 самых долгих запросов
    req_by_time_sorted = [(k, req_by_time[k]) for k in sorted(req_by_time, reverse=True)][:10]
    req_by_time_top = [v for k, v in req_by_time_sorted]
    # вычисляем топ 10 запросов которые завершились клиентской ошибкой
    client_errs_sorted = [(k, client_errs[k]) for k in sorted(client_errs, key=client_errs.get, reverse=True)][:10]
    client_errs_top = [make_errs_dict(k, v) for k, v in client_errs_sorted]
    # вычисляем топ 10 запросов которые завершились серверной ошибкой
    server_errs_sorted = [(k, server_errs[k]) for k in sorted(server_errs, key=server_errs.get, reverse=True)][:10]
    server_errs_top = [make_errs_dict(k, v) for k, v in server_errs_sorted]

    return {'total': total,
            'by_method': call_by_methods,
            'top_ip': ip_address_top,
            'top_request': req_by_time_top,
            'client_errs': client_errs_top,
            'server_errs': server_errs_top}


def create_info(line: str):
    regexp = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+"(GET|HEAD|POST|PUT|DELETE|PATCH) (.*) HTTP\/1\.\d{1}" (\d{3}) (\d{1,10}|-) "(.*)" "(.*)" (\d{1,10})'
    log_str = re.search(regexp, line)
    if log_str is None:
        return None
    ip = log_str.groups()[0]
    method = log_str.groups()[1]
    resource = log_str.groups()[2]
    code = int(log_str.groups()[3])
    try:
        bytes_cnt = int(log_str.groups()[4])
    except ValueError:
        bytes_cnt = -1
    from_address = log_str.groups()[5]
    user_agent = log_str.groups()[6]
    time_ms = int(log_str.groups()[7])
    info = LogLineInfo(ip, method, resource, code, bytes_cnt, from_address, user_agent, time_ms)
    return info


parser = argparse.ArgumentParser(description='Great Description To Be Here')
parser.add_argument('-logfile', action='store', dest='file', help='specify log file')
parser.add_argument('-logdir', action='store', dest='dir', help='specify log dir')
arg = parser.parse_args()

file_log = process(arg.file)
app_json = json.dumps(file_log, sort_keys=True, indent=4)
print(app_json)
