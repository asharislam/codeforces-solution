# 1551A	Polycarp and Coins using python by Ashar Islam

t = int(input())
for _ in range(t):
    n = int(input())
    x = n//3
    y = n%3

    if y == 0:
        c1, c2 = x, x
    elif y == 1:
        c1, c2 = x + 1, x
    else:
        c1, c2 = x, x + 1

    print(c1, c2)