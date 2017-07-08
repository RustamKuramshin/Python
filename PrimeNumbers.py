import time

number = int(input('Enter the number: '))
start = time.clock()  # Start Bench
for n in range(1, number, 2):
    for x in range(1, n, 2):
        if x == 1:
            continue
        if n % x == 0:
            #print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

end = time.clock() - start  # Stop Bench
print('Время выполнения составило', round(end, 3), 'секунд')
