# 1857A	Array Coloring using python by Ashar Islam

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    for i in range(1, len(s)+1):
        if sum(s[:i])%2 == sum(s[i:])%2:
            print("YES")
            break
        else:
            print("NO")
            break



# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = list(map(int, input().split()))
#
#     if sum(s) % 2 == 0:
#         print("YES")
#     else:
#         print("NO")