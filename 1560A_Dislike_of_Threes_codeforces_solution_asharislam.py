# 1560A	Dislike of Threes using python by Ashar Islam

t = int(input())
s = []
for _ in range(t):
    k = int(input())
    s.append(k)

max_k = max(s)

l = []
i = 1

for i in range(1, max_k * 3):
    if i % 3 != 0 and i % 10 != 3:
        l.append(i)
    if len(l) >= max_k:
        break

for i, k in enumerate(s):
    print(l[k - 1])