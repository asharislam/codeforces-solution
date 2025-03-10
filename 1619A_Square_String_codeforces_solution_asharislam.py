# 1619A	Square String? using python by Ashar Islam

# n = int(input())
# for _ in range(n):
#     s = input()
#     a = len(s)
#     b = int(a/2)
#     if s[:b] == s[b:] and a%b == 0:
#         print("YES")
#     else:
#         print("NO")


n = int(input())
for _ in range(n):
    s = input()
    a = len(s)
    if a % 2 == 0 and s[:a//2] == s[a//2:]:
        print("YES")
    else:
        print("NO")
