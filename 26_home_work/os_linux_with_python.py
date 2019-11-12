import argparse
import os
import subprocess


def execute_cmd(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    process.wait()
    return process.communicate()[0].decode()


def get_cpu_info():
    cpu_info = os.popen("cat /proc/cpuinfo").read().split('\n')
    cpu_info_dict = {}
    for line in cpu_info:
        if len(line.strip()) == 0:
            break
        k, v = line.split(':')
        cpu_info_dict[k.strip()] = v.strip()
    res = 'Model name: ' + cpu_info_dict['model name'] + '\n' \
          + 'Cache size: ' + cpu_info_dict['cache size'] + '\n' \
          + ''
    return res


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Params')
    parser.add_argument('-p', '--packet', action='store', default='GET')
    parser.add_argument('-d', '--dir', action='store', default='GET')
    arg = parser.parse_args()

    print("========= Сетевые интерфейсы =========\n", execute_cmd(["ip", "a"]))
    print("======== Маршрут по умолчанию ========\n", execute_cmd(["ip", "r"]))
    print("====== Информация о процессоре =======\n", get_cpu_info(), sep='')

    ps_info = [c for p, c in [x.rstrip('\n').split(' ', 1) for x in os.popen('ps h -eo pid:1,command')]]
    print("====== Список запущенных процессов =======\n", ps_info, sep='')

    print("========= Состояние сервиса cron =========\n", execute_cmd(["service", "cron", "status"]))
    print("========= Версия пакета {packet} =========\n".format(packet=arg.packet),
          execute_cmd(["apt", "policy", arg.packet]))
    print("========= Список файлов в директории =====\n", execute_cmd(["ls", "-h", arg.dir]), sep='')
    print("========= Текущая директория =====\n", execute_cmd("pwd"), sep='')
    print("========= Версия ядра =====\n", execute_cmd(["uname", "-r"]), sep='')
    print("========= Версия ОС =====\n", execute_cmd(["cat", "/proc/version"]), sep='')

