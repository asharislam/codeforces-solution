# 1807A	Plus or Minus using python by Ashar Islam

n = int(input())
for _ in range(n):
    s = list(map(int, input().split()))
    if sum(s[:2]) == s[2]:
        print("+")
    else:
        print("-")

# n = int(input())
# for _ in range(n):
#     s = list(map(int, input().split()))
#     print("+" if sum(s[:2]) == s[2] else "-")
