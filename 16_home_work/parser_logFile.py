import argparse
import json
import re
from collections import Counter

parser = argparse.ArgumentParser(description='Great Description To Be Here')
parser.add_argument('-logfile', action='store', dest='file', help='specify log file')
parser.add_argument('-logdir', action='store', dest='dir', help='specify log dir')
arg = parser.parse_args()

dist_ip = {}
dist_ip_count = {}
ips_list = []
log_line_str = ''
dist_log_line_str = {}
dict_by_http_code = {}


def reader_file(filename):
    # пробуем открыть файл для чтения, иначе ошибка
    try:
        with open(filename) as file:
            log = file.readlines()
        ip_num = 0
        for line in log:
            # регулярка для ip
            ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
            search = re.search(ip, line)
            ip_num += 1
            # регулярка для строки лога: группа для ip, метода, url, код ответа, время запроса
            logstr = re.search(
                r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+"(GET|POST|DELETE|PUT|HEAD) (.*") ([0-9]{3}) ([0-9].*)', line)
            # если в строке лога нет данных по ip пропускаем эту строку
            if search is None:
                continue
            # если в строке лога нет данных по  ip, методу, url, код ответа, время запроса пропускаем эту строку
            if logstr is None:
                continue
            ip_list = search.group()
            # список всех ip-ков из логов
            ips_list.append(ip_list)
            # регулярка по методу, если в строке лога не встретили метод пропускаем строку
            search = re.search(r'\] \"(GET|POST|DELETE|PUT|HEAD)', line)
            if search is None:
                continue
            # вытасткиваем из строки лога url, код ответа, время запроса, метод
            url = logstr.groups()[2]
            code = logstr.groups()[3]
            time_req = logstr.groups()[4]
            method = search.groups()[0]
            # записываем в строку полученные из лога данные
            log_line_str = ip_list + ' ' + method + ' ' + url + ' ' + time_req
            log_line_code = ip_list + ' ' + method + ' ' + url + ' ' + code
            # записываем в словарь данные с кодом ответа
            dist_log_line_str[int(time_req)] = log_line_str
            if dict_by_http_code.get(code) == None:
                dict_by_http_code[code] = list()
            dict_by_http_code[code].append(log_line_code)
            # считаем количество запросов по типу метода
            if dist_ip.get(ip, None) is None:
                dist_ip[ip] = {
                    'GET': 0,
                    'POST': 0,
                    'DELETE': 0,
                    'PUT': 0,
                    'HEAD': 0
                }
            dist_ip[ip][method] += 1
        # преобразуем список ip-ков в словарь с указанием количества  ip-ков
        dist_ip_count = Counter(ips_list)
        # выбираем 5 ip-ков с наиблоьшим числом обращений
        output_max_ip = dict(dist_ip_count.most_common()[:5])
        # формируем данные со временем  долгих запросов, выбираем 5 записей
        # список со временем
        keys = list(dist_log_line_str.keys())
        keys.sort(reverse=True)
        keys = keys[:5]
        output_max_time_req = ''
        for key in keys:
            output_max_time_req += dist_log_line_str[key] + '\n'
        # формируем по запросам с ошибками, выбираем из них 5 штук
        errors = list()
        for code in dict_by_http_code:
            if code != '200':
                errors.extend(dict_by_http_code[code])
        output_code_error = "\n".join(errors[:5])
        # выводим на печать
        print("количество общее количество выполненных запросов: " + ip_num.__str__())
        print(json.dumps(dist_ip, indent=4))
        print(" топ 5 IP адресов, с которых были сделаны запросы: ")
        print(output_max_ip)
        print(" топ 5 IP адресов,  самых долгих запросов: ")
        print(output_max_time_req)
        print(" запросов, которые завершились ошибкой: ")
        print(output_code_error)
    except IOError:
        print("Error: File does not appear to exist.")


reader_file(arg.file)
