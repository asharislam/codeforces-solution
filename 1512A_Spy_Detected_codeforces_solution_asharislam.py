# 1512A	Spy Detected! using python by Ashar Islam

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    if s[0] == s[1]:
        x = s[0]
    else:
        if s[0] == s[2]:
            x = s[0]
        else:
            x = s[1]
    for i in range(n):
        if s[i] != x:
            print(i+1)
            break