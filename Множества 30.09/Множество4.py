first = "0 0 0 0 0 0 0"
second = "1 1 1 0 0 0 0"
third = "1 1 1 1 1 1 1"
n = input().split()
for i in range(len(n)): n[i] = int(n[i])
a, b, c, d, e, f, g = n
print(a + b + c - d - e - f + g)
