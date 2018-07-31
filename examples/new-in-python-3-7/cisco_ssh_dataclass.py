import netmiko
from dataclasses import dataclass, field

@dataclass(frozen=True)
class CiscoSSH:
    ip: str
    username: str
    password: str = field(repr=False)
    secret: str = field(repr=False)

    def __post_init__(self):
        print('Подключаюсь к {}'.format(self.ip))
        device_dict = {'device_type':'cisco_ios',
                       'username': self.username,
                       'password': self.password,
                       'secret': self.secret,
                       'ip': self.ip }
        self.ssh = netmiko.ConnectHandler(**device_dict)
        self.ssh.enable()

    def send_command(self, command):
        result = self.ssh.send_command(command)
        return result

