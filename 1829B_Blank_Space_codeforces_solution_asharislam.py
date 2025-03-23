# 1829B	Blank Space using python by Ashar Islam

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    a = 0
    b = 0

    for i in s:
        if i == 0:
            b += 1
            a = max(a, b)
        else:
            b = 0

    print(a)
