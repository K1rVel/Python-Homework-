import game
while True:
    start = input('Чтобы начать игру, введите "start", чтобы завершить игру введите "0": ')
    if start == 0:
        print('Игра завершена')
    else:
        game.main(start)
