from random import randint
n = [0,0]
while True:
	if input() == 'off': break
	a = randint(1,2)
	n[a-1] += 1
	print(f'Ваш номер: {a}\nУчастников в первом забеге: {n[0]}, Участников во втором забеге: {n[1]}')