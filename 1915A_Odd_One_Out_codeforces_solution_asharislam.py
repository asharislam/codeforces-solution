# 1915A - Odd One Out using python by Ashar Islam

n = int(input())
for _ in range(n):
    s = list(map(int, input().split()))
    if s[0] == s[1]:
        print(s[2])
    elif s[1] == s[2]:
        print(s[0])
    else:
        print(s[1])

