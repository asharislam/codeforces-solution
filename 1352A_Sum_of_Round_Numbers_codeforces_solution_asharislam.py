# 1352A	Sum of Round Numbers using python by Ashar Islam

# n = int(input())
# for i in range(n):
#
#     s = list(input().strip())
#     total = 0
#     k = []
#
#     for j in range(len(s)):
#         if s[j] != "0":
#             k.append(s[j] + ((len(s)-j-1)*"0"))
#             total +=1
#
#     print(total)
#     print(" ".join(k))


# Another way
n = int(input())
for _ in range(n):
    s = input().strip()
    k = []

    for i, digit in enumerate(reversed(s)):

        if digit != '0':
            k.append(str(int(digit) * (10 ** i)))

    print(len(k))
    print(" ".join(k))
