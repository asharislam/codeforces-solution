n = int(input())
s = []
for _ in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)

    z = x%y
    if z ==0:
        s.append(0)
    else:
        s.append(y-z)
for i in s:
    print(i)