import os
import datetime
import re
import socket


class NetFlowData:
    def __init__(self, strNetFlow):
        self.Start = re.findall(r"[\w']+", strNetFlow[0])
        self.End = re.findall(r"[\w']+", strNetFlow[1])

        # Вычислим длительность соединения
        year = 2017
        StartTime = datetime.datetime(year, int(self.Start[0][0:2]), int(self.Start[0][2:4]), int(self.Start[1]),
                                      int(self.Start[2]), int(self.Start[3]), int(self.Start[4]))
        EndTime = datetime.datetime(year, int(self.End[0][0:2]), int(self.End[0][2:4]), int(self.End[1]),
                                    int(self.End[2]), int(self.End[3]), int(self.End[4]))

        self.Dur = EndTime - StartTime

        self.SrcIPaddress = strNetFlow[3]
        self.SrcP = int(strNetFlow[4])
        self.DstP = strNetFlow[7]
        self.Pkts = strNetFlow[9]


TotalPkts = 0
WebPkts = 0
UniqIP = set()
UniqIP_1sec = set()
TotalTelnet = 0
TotalSSH = 0
TotalFTP = 0
TotalDNS = 0
TotalTV = 0
DynamicPort = 0
UniqNoDNS = set()
OneSecPkts = 0
TotalConn = 0

for file in os.listdir():
    if file.find('txt') != -1:
        print('Анализ файла ', file)
        print()
        with open(file) as NetFlow:

            counter = 0

            # Циклический обход строк файла
            for line in NetFlow.readlines():
                list_col = line.split()
                if (counter > 1) and (len(list_col) == 10):

                    # Общее количество соединений
                    TotalConn += 1

                    print('Строка ', TotalConn)
                    print(line)

                    NetFlowObj = NetFlowData(list_col)

                    # Общее входящего трафика +
                    TotalPkts += int(NetFlowObj.Pkts)

                    # Объем web-трафика +
                    if (NetFlowObj.SrcP == 80) or (NetFlowObj.SrcP == 443):
                        WebPkts += int(NetFlowObj.Pkts)

                    # Общее количество уникальных IP-адресов отправвителя +
                    UniqIP.add(NetFlowObj.SrcIPaddress)

                    # Общее количество уникальных IP-адресов отправителя,
                    # по которым время соединения не привышает 1секунды +
                    delta = datetime.timedelta(seconds=1)
                    if NetFlowObj.Dur < delta:
                        UniqIP_1sec.add(NetFlowObj.SrcIPaddress)
                        OneSecPkts += int(NetFlowObj.Pkts)

                    # Общее количество попыток подключения по Telnet +
                    if NetFlowObj.DstP == '23':
                        TotalTelnet += 1

                    # Общее количество попыток подключения по SSH +
                    if NetFlowObj.DstP == '22':
                        TotalSSH += 1

                    # Общее количество попыток подключения на FTP +
                    if (NetFlowObj.DstP == '21') or (NetFlowObj.DstP == '20'):
                        TotalFTP += 1

                    # Общее количество попыток подключения к DNS +
                    if NetFlowObj.DstP == '53':
                        TotalDNS += 1

                    # Объем трафика TeamViewer +
                    if NetFlowObj.SrcP == 5938:
                        TotalTV += int(NetFlowObj.Pkts)

                    # Общее количество подключений с динамических портов
                    if NetFlowObj.SrcP > 49152:
                        DynamicPort += 1

                    # Количество уникальных IP-адресов, неимеющих DNS-имени
                    # try:
                    #     socket.gethostbyaddr(NetFlowObj.SrcIPaddress)
                    # except socket.herror:
                    #     UniqNoDNS.add(NetFlowObj.SrcIPaddress)

                counter += 1

print()
print('**************************Результаты анализа детализации трафика по данным NetFlow******************************')
print()
print('Статистика за период детализации входящего трафика')
print()
print('Объем входящего трафика: %d пакетов' % TotalPkts)
print('Объем web-трафика: %d пакетов' % WebPkts)
print('Количество уникальных IP-адресов отправителя: %d' % len(UniqIP))
print('Количество уникальных IP-адресов, по которым время соединения не превышало 1 секунды: %d. ' % len(UniqIP_1sec), end='')
print('Вклад в общий трафик по таким адресам: %d пакетов' % OneSecPkts)
print('Количество попыток подключения на 23 порт Telnet: %d' % TotalTelnet)
print('Количество попыток подключения на 22 порт SSH: %d' % TotalSSH)
print('Количество попыток подключения на 21 или 22 порты FTP: %d' % TotalFTP)
print('Количество попыток подключения на 53 порт DNS: %d' % TotalDNS)
print('Объем трафика TeamViewer c 5938 порта: %d' % TotalTV)
print('Количество подключений с динамических портов: %d' % DynamicPort)
print('Общее количество соединений: %d' % TotalConn)
print('Количество уникальных IP-адресов, неимеющих DNS-имени: %d' % len(UniqNoDNS))
