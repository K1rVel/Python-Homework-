import os

spisok_1 = (os.listdir(r"C:\Users\user\Desktop\123\target"))

for i in spisok_1:
    if int(i) % 2 == 0:
        os.rename(fr"C:\Users\user\Desktop\123\target\{i}", fr"C:\Users\user\Desktop\123\target\1234{i}")