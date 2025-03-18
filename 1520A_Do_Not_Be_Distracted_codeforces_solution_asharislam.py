# 1520A	Do Not Be Distracted! using python by Ashar Islam

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    y = set()
    x = ''
    z = False

    for i in s:
        if i != x:
            if i in y:
                z = True
                break
            y.add(i)
        x = i

    if z:
        print("NO")
    else:
        print("YES")