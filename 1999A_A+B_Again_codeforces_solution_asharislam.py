# 1999A	A+B Again? using python by Ashar Islam

n = int(input())
for _ in range(n):
    s = list(map(int, input().strip()))
    print(sum(s))


n = int(input())
for _ in range(n):
    s = input().strip()
    print(int(s[0]) + int(s[1]))