# -*- coding: utf-8 -*-
'''
Задание 8.1a

Переделать декоратор retry: добавить параметр delay, который контролирует через какое количество секунд будет выполняться повторная попытка.

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

