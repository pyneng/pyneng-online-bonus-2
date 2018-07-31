# -*- coding: utf-8 -*-
'''
Задание 8.1

Создать декоратор retry, который выполняет декорируемую функцию повторно, заданное количество раз, если результат функции не был истинным.

Пример работы декоратора:
In [20]: @retry(times=3)
    ...: def send_show_command(device, show_command):
    ...:     print('Подключаюсь к', device['ip'])
    ...:     try:
    ...:         with ConnectHandler(**device) as ssh:
    ...:             ssh.enable()
    ...:             result = ssh.send_command(show_command)
    ...:         return result
    ...:     except SSHException:
    ...:         return False
    ...:

In [21]: send_show_command(r1_params, 'sh clock')
Подключаюсь к 192.168.100.1
Out[21]: '*14:22:01.566 UTC Mon Mar 5 2018'

In [22]: r1_params['password'] = '123123'

In [23]: send_show_command(r1_params, 'sh clock')
Подключаюсь к 192.168.100.1
Подключаюсь к 192.168.100.1
Подключаюсь к 192.168.100.1
Подключаюсь к 192.168.100.1
Out[23]: False

'''

from netmiko import ConnectHandler
from paramiko.ssh_exception import SSHException

r1_params = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.1',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}


def send_show_command(device, show_command):
    print('Подключаюсь к', device['ip'])
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(show_command)
        return result
    except SSHException:
        return False


if __name__ == "__main__":
    output = send_show_command(r1_params, 'sh clock')

