name = input("Введите имя - ")
test = [lambda name: "Гений " + name, lambda name: "Сверхразум " + name, lambda name: "Просто " + name]
gen = ['а', 'я', 'г', 'м']
over = ['о', 'ь', 'л', 'н']
if name[-1] in gen:
    print(test[0](name))
elif name[-1] in over:
    print(test[1](name))
else:
    print(test[2](name))