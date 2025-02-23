# 490A - Team Olympiad using python by Ashar Islam

n = int(input())
s = list(map(int, input().split()))

p = []
m = []
pe = []
for i in range(n):
    if s[i] == 1:
        p.append(i+1)
    elif s[i] == 2:
        m.append(i+1)
    elif s[i] == 3:
        pe.append(i+1)
final = min(len(p), len(m), len(pe))
print(final)

if final > 0:
    for i in range(final):
        print(p[i], m[i], pe[i])