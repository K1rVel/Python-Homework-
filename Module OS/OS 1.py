import os

print("Операционная система - " + os.name)
print("Имя компьютера - " + os.environ.get("COMPUTERNAME"))
print("Имя пользователя - " + os.environ.get("USERNAME"))