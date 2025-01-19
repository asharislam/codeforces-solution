m = input().split()
n = int(m[0])
t = int(m[1])
s = input()
k = list(s)

for _ in range(t):
    i = 0
    while i < len(k) - 1:
        if k[i] == 'B' and k[i + 1] == 'G':
            k[i], k[i + 1] = k[i + 1], k[i]
            i += 1
        i += 1
print(''.join(k))