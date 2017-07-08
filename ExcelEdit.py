import win32com.client
import os

BadCodes = []
excel = win32com.client.Dispatch('Excel.Application')

wb = excel.Workbooks.Open(os.getcwd() + r'\ВыгрузкаДляБерловксойExcel.xls')
sheet = wb.ActiveSheet
endrow = sheet.UsedRange.Rows.Count

with open("BadCodes.txt") as file:
    for line in file.readlines():
        BadCodes.append(line.rstrip())

i = 0
for row in range(2, endrow):

    cell = sheet.Range('A{}'.format(row)).value
    cell = str(int(cell))
    cell.rstrip()

    try:

        if cell in BadCodes:
            print('Строка ' + str(row) + ' будет отмечена на удаление! Штрихкод: ' + cell)
            sheet.Range('A{}'.format(row)).value = 'DEL'
            i += 1

    except Exception:

        print('Неизвестная ошибка')

print('Было отмечено на удаление ' + str(i) + ' строк')
wb.Save()
wb.Close()
