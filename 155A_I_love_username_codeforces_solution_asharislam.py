# 155A	I_love_\%username\% using python by Ashar Islam

n = int(input())
s = list(map(int, input().split()))

best = s[0]
worst = s[0]
total = 0

for i in range(1, n):
    if s[i] > best:
        best = s[i]
        total += 1
    elif s[i] < worst:
        worst = s[i]
        total += 1

print(total)
