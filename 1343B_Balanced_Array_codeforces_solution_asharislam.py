# 1343B	Balanced Array using python by Ashar Islam

n = int(input())

for _ in range(n):
    s = int(input())
    if (s // 2) % 2 == 1:
        print("NO")
    else:
        print("YES")

        e = []
        o = []
        for i in range(1, (s // 2) + 1):
            e.append(2 * i)
        for i in range(1, (s // 2)):
            o.append(2 * i - 1)
        o.append(sum(e) - sum(o))
        print(*e, *o)
