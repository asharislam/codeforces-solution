# 1367B	Even Array using python by Ashar Islam

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    o = 0
    e = 0
    for i in range(n):
        if i %2 == 0 and s[i] % 2 != 0:
            o +=1
        elif i%2 == 1 and s[i]%2 == 0:
            e +=1
    if o == e:
        print(o)
    else:
        print(-1)
