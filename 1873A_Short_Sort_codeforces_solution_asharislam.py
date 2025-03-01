# 1873A - Short Sort using python by Ashar Islam

n = int(input())
k = ["abc", "acb", "bac", "cba"]
for _ in range(n):
    s = input().strip()
    if s in k:
        print("YES")
    else:
        print("NO")


# n = int(input())
# k = ["abc", "acb", "bac", "cba"]
# for _ in range(n):
#     s = input()
#     if s in k:
#         print("YES")
#     else:
#         print("NO")


# t = int(input().strip())
# for _ in range(t):
#     s = input().strip()
#     if s in ["abc", "acb", "bac", "cba"]:
#         print("YES")
#     else:
#         print("NO")



# n = int(input())
# for _ in range(n):
#     s = input()
#     if s == "abc" or s == "acb" or s == "bac" or s == "cba":
#         print("YES")
#     else:
#         print("NO")


# n = int(input())
# for _ in range(n):
#     s = input()
#     print("YES" if s == "abc" or s == "acb" or s == "bac" or s == "cba" else "NO")
