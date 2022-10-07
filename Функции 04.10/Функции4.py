def IMT():
    weight = int(input("введите вес"))
    height = int(input("введите рост"))
    b = height **2
    a = weight/b
    return a


def IMT_Count(a):
    if a < 18.5:
        print("недостаточный вес")
    elif a >= 18.5 and a <= 25:
        print("нормальный вес")
    elif a >25:
        print("избыточный вес")


IMT_Count(IMT())