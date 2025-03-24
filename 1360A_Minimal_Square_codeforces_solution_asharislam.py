# 1360A	Minimal Square using python by Ashar Islam

# t = int(input())
# for _ in range(t):
#     s = list(map(int, input().split()))
#
#     x = s[0]*2, s[1]
#     a = max(x)**2
#     y = s[0], s[1]*2
#     b = max(y)**2
#
#     z = s[0] + s[1]
#     c = max(s)
#     d = max(z, c)
#     e = d**2
#
#     print(min(a, b, e))


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    x = max(2 * a, b) ** 2
    y = max(a, 2 * b) ** 2
    z = max(a + b, max(a, b)) ** 2

    print(min(x, y, z))
