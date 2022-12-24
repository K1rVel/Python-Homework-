import csv

with open("Task1.csv", "r") as f:
    reader = csv.reader(f, delimiter=";")
    for row in list(reader):
        print(f"{row[1]} {row[3]}")