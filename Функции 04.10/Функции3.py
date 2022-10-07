def passage(score):
		print(score>50)
		return score>50
for i in range(int(input('Введите число учеников: '))):
	if passage(int(input('Введите свой балл: '))) == False:
		print('Вы отчислены')