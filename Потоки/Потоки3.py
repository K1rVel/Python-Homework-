import time
from threading import Thread

def faster():
    while True:
        print('Вводите быстрее')
        time.sleep(3)


th = Thread(target=faster, daemon=True)
th.start()
x = int(input('Ввод кода от бомбы: '))
if x == 1234:
    print('Бомба разминирована')
else:
    print('Вы взорвались')