# 1433A	Boring Apartments using python by Ashar Islam

n = int(input())
for _ in range(n):
    s = list(map(int, input().strip()))
    d = s[0]
    k = len(s)
    result = (d - 1) * 10 + (k * (k + 1)) // 2
    print(result)