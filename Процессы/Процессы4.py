from multiprocessing import Process, Pipe
from time import sleep
from random import randint

num = randint(1, 10)
time = 3


def subscription(time, conn):
    while time != 0:
        sleep(1)
        time -= 1
    print("\nВаша подписка закончилась.")
    conn.send(True)
    conn.close()
    return


def game(num, conn):
    count = 1
    while True:
        if conn.poll():
            conn.close()
            return
        inp = int(input("Введите загаданное число: "))
        if inp == num:
            print(f"Вы угадали число с {count} попытки(ок)")
            sleep(0.5)
            num2 = randint(1, 10)
            return game(num2, conn)
        else:
            count += 1
            print("Играть ещё раз?")
            sleep(0.5)


if __name__ == "__main__":
    first_part_of_pipe, second_part_of_pipe = Pipe()
    p1 = Process(target=subscription, args=(time, first_part_of_pipe), daemon=True)
    p1.start()
    game(num, second_part_of_pipe)