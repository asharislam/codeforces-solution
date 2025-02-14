# 1760A	Medium Number using python by Ashar Islam

n = int(input())
for _ in range(n):
    s = sorted(list(map(int, input().split())))
    print(s[1])
