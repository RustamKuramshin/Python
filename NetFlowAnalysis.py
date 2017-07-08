import re

ip = set()
i = 0
packages = 0
pattern = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")  # [0-9.:]+
with open('netflow.txt', 'r') as file:
    for line in file.readlines():
        lst = pattern.findall(line)
        s = line.split()
        if len(lst) == 2:
            print(line)
            packages += int(s[-1])
            ip.add(lst[0])
            i += 1

print('Всего %d соединений' % i)
print('Уникальных ip-адресов %d' % len(ip))
print('Всего принято пакетов %d' % packages)
