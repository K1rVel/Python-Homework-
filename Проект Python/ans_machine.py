def main(input):
    if 'распи' in input.lower():
        timetable()
    if 'трени' in input.lower():
        tian()
    if 'оплата' in input.lower():
        link()
    if 'назва' in input.lower():
        slan()
    if 'сайт' in input.lower():
        sool()


def timetable():
    print('Часы работы спортзала Пн - с 10:00 до 22:00 Ср - 10:00 до 22:00 Пт - 10:00 до 22:00')
    print('Вы хотите посетить тренировку? Введите - да/нет')
    t1=input()
    s1={}
    if t1=='да':
        print('Выберите удобный для вас день недели')
        t2=input()
        print('Введите удобное для вас время с 10:00 до 22:00')
        t3=int(input())
        if 8<=t3<=23:
            s1[t2]=t3
            print('Вы записались на', s1)
def tian():
    print('Хорошей, вам, тренировки!')
def link():
    print('К оплате за месяц - 4500')
def slan():
    print('ООО ДАВИНЧИ г. Сочи, ул. Ленина, д.10')
def sool():
    print('https://en.wikipedia.org/wiki/KK')