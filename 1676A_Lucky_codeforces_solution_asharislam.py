# 1676A	Lucky? using python by Ashar Islam

n = int(input())
for _ in range(n):
    s = list(map(int, input().strip()))
    if s[0]+s[1]+s[2] == s[3]+s[4]+s[5]:
        print("YES")
    else:
        print("NO")


# n = int(input())
# for _ in range(n):
#     s = list(map(int, input().strip()))
#     print("YES" if s[0]+s[1]+s[2] == s[3]+s[4]+s[5] else "NO")

# n = int(input())
# for _ in range(n):
#     s = [int(i) for i in input().strip()]
#     print("YES" if sum(s[:3]) == sum(s[3:]) else "NO")

# n = int(input())
# for _ in range(n):
#     s = list(map(int, input().strip()))
#     if sum(s[3:]) == sum(s[:3]):
#         print("YES")
#     else:
#         print("NO")

# n = int(input())
# print("\n".join(["YES" if sum(s[:3]) == sum(s[3:]) else "NO" for s in [[int(i) for i in input().strip()] for _ in range(n)]]))

