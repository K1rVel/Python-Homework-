import time
from threading import Thread

def alarm():
    x = input('Напоминание:\n')
    y = int(input('Время:\n'))
    time.sleep(y)

    print(x)


th = Thread(target=alarm, daemon=True)
th.start()
time.sleep(30)
print('Программа завершается')