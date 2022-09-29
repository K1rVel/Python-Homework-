a = int(input())
b = int(input())
c = int(input())
if a < b and b < c:
    print('Акция!', 'К оплате:')
    print((a + b + c)/2)
elif c < b and b < a:
    print('Акция!','К оплате:')
    print((a + b + c)/3)
else:
    print('К оплате:', a + b + c)
