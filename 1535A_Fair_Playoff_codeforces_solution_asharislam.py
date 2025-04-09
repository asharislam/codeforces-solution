# 1535A	Fair Playoff using python by Ashar Islam

# t = int(input())
# for _ in range(t):
#     s = list(map(int, input().split()))
#     x = s[:2]
#     y = s[2:]
#
#     if max(x) > min(y) and max(y) > min(x):
#         print("YES")
#     else:
#         print("NO")

t = int(input())
for _ in range(t):
    s = list(map(int, input().split()))

    if max(s[:2]) > min(s[2:]) and max(s[2:]) > min(s[:2]):
        print("YES")
    else:
        print("NO")
