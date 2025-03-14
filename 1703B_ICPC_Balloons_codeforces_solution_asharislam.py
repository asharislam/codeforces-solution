# 1703B	ICPC Balloons using python by Ashar Islam

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(str, input().strip()))
    k = []
    for i in s:
        if i not in k:
            k.append(i)
    print((len(k)*2) + n - len(k))

#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = input().strip()
#
#     k = set()
#     total = 0
#
#     for i in s:
#         if i not in k:
#             total += 2
#             k.add(i)
#         else:
#             total += 1
#
#     print(total)


