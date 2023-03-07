import time
from threading import Thread

def sleepMe(i):
    print("Поток %i заснул на 3 секунды.\n" % i)
    time.sleep(5)
    print("Поток %i просыпается.\n" % i)
for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()