# 268A_Games using python by Ashar Islam

n = int(input())
x = []
y = []
total = 0

for _ in range(n):
    p, q = map(int, input().split())
    x.append(p)
    y.append(q)

for i in range(n):
    for j in range(n):
        if x[i] == y[j]:
            total +=1

print(total)