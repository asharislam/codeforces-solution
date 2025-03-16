# 1283A	Minutes Before the New Year using python by Ashar Islam


n = int(input())
for _ in range(n):
    s = list(map(int, input().split()))
    h = ((24 - s[0])*60)-s[1]
    print(h)


# n = int(input())
# for _ in range(n):
#     h, m = map(int, input().split())
#     result = (23 - h) * 60 + (60 - m)
#     print(result)
