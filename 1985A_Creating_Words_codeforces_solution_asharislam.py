# 1985A - Creating Words using python by Ashar Islam

n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    print(b[0]+a[1]+a[2], a[0]+b[1]+b[2])


# n = int(input())
# for _ in range(n):
#     a, b = map(str, input().split())
#     print(b[0]+a[1:], a[0]+b[1:])