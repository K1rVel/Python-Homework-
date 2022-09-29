a = input().split(', ')
n = ['5','3','4']
u = 0
for elem in n:
	u += a.count(elem)
print(a, len(a), u / len(a) * 100)
