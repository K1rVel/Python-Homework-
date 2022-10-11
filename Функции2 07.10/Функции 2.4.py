def rec(ans = 0):
    n = input()
    if n == '':
        return ans
    ans += int(n)
    return rec(ans)


print(rec())