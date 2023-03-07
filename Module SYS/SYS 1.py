import sys

list = []
for i in sys.argv:
    list.append(i)
if list[1] == '--name':
    print('Hello', list[2])
else:
    print('Hello world')