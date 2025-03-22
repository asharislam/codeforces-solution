# 1873B	Good Kid using python by Ashar Islam

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total = 0

    for i in range(n):
        x = a[i]
        a[i] += 1

        product = 1
        for j in a:
            product *= j

        total = max(total, product)
        a[i] = x

    print(total)