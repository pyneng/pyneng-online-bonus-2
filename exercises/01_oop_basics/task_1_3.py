# -*- coding: utf-8 -*-

'''
Задание 1.3

Дополнить любой из вариантов класса CiscoSSH из заданий 1.2a-1.2d.

Добавить метод, который закрывает сессию SSH при удалении объекта.

Пример использования:
In [4]: r1 = CiscoSSH('cisco', 'cisco', 'cisco', '192.168.100.1')

In [5]: r1.send_show_command('sh clock')
Out[5]: '*11:19:39.596 UTC Sun Jan 14 2018'

In [6]: del r1
Соединение разорвано

```

