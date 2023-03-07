import random
from queue import Queue
from concurrent.futures import ThreadPoolExecutor


def numbers_1(queue, number):
    for i in range(1, number + 1):
        num = random.randint(1, 10)
        queue.put(num)


def delenie(queue):
    while not queue.empty():
        num = queue.get()
        list_1 = []
        for i in range(1, num + 1):
            if num % i == 0:
                list_1.append(i)
        print(f"{list_1} - делители числа {num}")


def main():
    with ThreadPoolExecutor() as Th:
        Th.submit(numbers_1, queue, number)
        Th.submit(delenie, queue)
        Th.submit(delenie, queue)


queue = Queue()
number = int(input("Введите количество чисел - "))

main()
print("Программа завершена")