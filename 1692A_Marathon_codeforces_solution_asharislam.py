# 1692A	Marathon using python by Ashar Islam

n = int(input())

for _ in range(n):
    s = list(map(int, input().split()))
    total = 0

    for i in range(1, len(s)):
        if s[0]<s[i]:
            total +=1
        else:
            pass
    print(total)

# comprehension
# n = int(input())
#
# for _ in range(n):
#     s = list(map(int, input().split()))
#     print(sum(1 for i in s[1:] if s[0] < i))


# using while loop
# n = int(input())
#
# count = 0
# while count < n:
#     s = list(map(int, input().split()))
#     total = 0
#     i = 1
#     while i < len(s):
#         if s[0] < s[i]:
#             total += 1
#         i += 1
#     print(total)
#     count += 1