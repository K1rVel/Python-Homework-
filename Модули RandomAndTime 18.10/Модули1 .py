from time import *
def chess():
	if time() - start >= 1800 or input('Введите ход: ') == 'off': return 0
	print('Осталось', round((1800-(time()-start))/60), 'минут')
	chess()
start = time()
chess()