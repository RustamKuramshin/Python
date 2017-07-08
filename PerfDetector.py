import psutil
from time import ctime

def detector():
    global previous
    detector = [' '*6 for i in range(nCores)]
    for j in range(nCores):
        if (loadCores[j] >= threshold) and (previous[j]!='begin'):
            detector[j] = 'begin'
            previous[j]=detector[j]
        elif (loadCores[j] < threshold) and (previous[j]!='end') and (previous[j]!='      '):
            detector[j] = 'end'
            previous[j]=detector[j] 
    return detector
            
def print_row():
    for i in range(nCores):
        print(loadCores[i],event[i], end = ' ')
    print(time_now, end = ' ')    
    print()

def rec_log():
    global log
    for i in range(nCores):
        if event[i] == 'begin':
            log.append(str(i))
            log.append(time_now)
            log.append('excess '+str(loadCores[i]))
            log.append(str(point))
        elif event[i] == 'end':
            log.append(str(i))
            log.append(time_now)
            log.append('normalization '+str(loadCores[i]))
            log.append(str(point))
            

def print_log():
    #if len(log) == 0:
        #print('Все ОК!')
    stop = len(log)-3
    for i in range(0,stop,4):
        print('core_'+ log[i] + '    ' + log[i+1] + '    ' + log[i+2] + '  ' + log[i+3])
    
            


time = int(input('Укажите интервал наблюдений в секундах: '))
threshold = float(input('Укажите порог срабатывания: '))

nCores = len(psutil.cpu_percent(interval=1,percpu=True))
previous = [' '*6 for j in range(nCores)]
log = []
point = 0

print('Начинаем анализ производительности ядер процессора...')
print('Старт в ' + ctime())

for i in range(time):
    point = i + 1
    time_now = ctime()
    loadCores = psutil.cpu_percent(interval=1,percpu=True)
    event = detector()
    #print_row()
    rec_log()
    print_log()
input('Введите Enter')
