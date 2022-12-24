import csv
import csv1

list = [["Предмет", "Преподаватель", "Любовь к предмету"],
          ["Основы алгоритмизации", "Иван Геннадьевич Шабрашин", "10"],
          ["Программирование", "Олег Юрьевич Бабченок", "10"],
          ["Английский язык", "Элина Рамилевна Биккинина", "10"],
          ["Физкультура", "Николай Анатольевич Соснин", "10"]]

with open("My.csv", "w+") as f:
    writer = csv.writer(f, delimiter=";")
    for i in spisok:
        writer.writerow(i)

    f.seek(0)

    reader = csv.reader(f)
    for row in list(reader):
        print(row)