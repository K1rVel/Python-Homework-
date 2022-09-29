a = int(input())
b = 0
c = a
while a > 0:
    b = a % 10 + b
    a = a//10
if c % 10 % 2 == 0 and b % 3 == 0:
    print('делится')

