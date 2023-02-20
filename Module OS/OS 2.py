import os

os.mkdir(r"C:\Users\user\Desktop\123\target")
os.chdir(r"C:\Users\user\Desktop\123\target")

for i in range(1, 17):
    os.mkdir(f"{i}")