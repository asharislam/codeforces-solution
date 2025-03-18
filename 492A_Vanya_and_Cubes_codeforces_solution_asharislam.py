# 492A	Vanya and Cubes using python by Ashar Islam

n = int(input())
c = 0
h = 0

for i in range(1, n + 1):
    k = (i * (i + 1)) // 2
    if c + k > n:
        break
    c += k
    h += 1

print(h)
