from multiprocessing import Process, Pipe


def pip(conn, val):
    conn.send(int(val) * 75)
    conn.close()


if __name__ == '__main__':
    val = input('Введите количество валюты: ')
    while val != 'off':
        mama_conn, sin_conn = Pipe()
        p = Process(target=pip, args=(sin_conn, val))

        p.start()
        print(mama_conn.recv())
        p.join()
        val = input('Введите количество валюты: ')