# 1335A - Candies and Two Sisters using python by Ashar Islam

n = int(input())
s = [0] * n

for j in range(n):
    x = int(input())
    s[j] = (x - 1) // 2
for i in s:
    print(i)


# Another way
# t = int(input())
# results = []
#
# for _ in range(t):
#     n = int(input())
#     if n <= 1:
#         results.append(0)
#     else:
#         results.append((n - 1) // 2)
#
# print("\n".join(map(str, results)))
