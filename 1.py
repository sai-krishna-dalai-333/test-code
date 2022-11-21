def base3(n):
    s = ""
    while (n > 0):
        r = n % 3
        s += str(r)
        n = n // 3
    s = s[::-1]
    return s
n=int(input())
print(base3(n))