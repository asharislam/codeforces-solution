# 1829A	Love Story using python by Ashar Islam

n = int(input())
k = ['c', 'o', 'd', 'e', 'f', 'o', 'r', 'c', 'e', 's']

for _ in range(n):
    total = 0
    s = list(input().strip())
    for i, j in zip(s, k):
        if i != j:
            total += 1
    print(total)
