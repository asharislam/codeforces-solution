# 1374A	Required Remainder using python by Ashar Islam

# t = int(input())
# for _ in range(t):
#     s = list(map(int, input().split()))
#     x = s[0]
#     y = s[1]
#     n = s[2]
#     k = (int((n - y)/x))*x+y
#     print(k)

t = int(input())
for _ in range(t):
    x, y, n = list(map(int, input().split()))
    k = (n-y)// x*x+y
    print(k)
