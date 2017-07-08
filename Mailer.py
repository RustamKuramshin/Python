#!/usr/bin/env python3

# Установить атрибут исполнимости "sudo chmod +x sender.py"
# Запуск скрипта из каталога, в котором он лежит "./sender.py ...абсолютный путь к файлу..."

import smtplib
import sys
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

def send_mail(send_from, send_to, subject, text, server, user_name, user_passwd, files = None):

    msg = MIMEMultipart()
    msg['From'] = # Строка от кого
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))


    with open (files, 'rb') as file:
        part = MIMEApplication(
            file.read(),
            Name=basename(files)
        )
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(files)
        msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.starttls()
    smtp.login(user_name, user_passwd)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

send_from = # почта отправителя
send_to = # почта получателя
subject = # тема
text = # тело письма
file = sys.argv[1]
server = # IP-адрес почтового сервера
user_name = # ученая запись на почтовом сервере
user_passwd = # пароль учетной записи

send_mail(send_from, send_to, subject, text, server, user_name, user_passwd, file)
