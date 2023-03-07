from threading import Thread
from queue import Queue
from time import sleep

queue = Queue()


def kick(queue):
    inp = ''
    sleep(2)
    while inp != "off":
        inp = input("Введите имя студента: ")
        queue.put(inp)
        sleep(2)


def bye(queue):
    while True:
        student = queue.get()
        if student != "":
            print(f"Студент {student} отчислен")
        else:
            print("Произошла ошибка")
        queue.task_done()
        sleep(1)


def main():
    for i in ["Смирнов", "Попов"]:
        queue.put(i)

    bye_stram = Thread(target=bye, args=(queue,))
    bye_stram.start()

    kik_stram = Thread(target=kick, args=(queue,))
    kik_stram.start()


main()