# 750A - New Year and Hurry using python by Ashar Islam

m = list(map(int, input().split()))
n = m[0]
s = 240 - m[1]
total = 0
k = 0 #time_spent

for i in range(1, n + 1):
    k += 5 * i
    if k <= s:
        total += 1
    else:
        break

print(total)