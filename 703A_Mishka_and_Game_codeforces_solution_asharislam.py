# 703A	Mishka and Game using python by Ashar Islam

n = int(input())
m = 0
c = 0
for _ in range(n):
    s = list(map(int, input().split()))
    if s[0] > s[1]:
        m +=1
    elif s[0] < s[1]:
        c +=1

if m > c:
    print("Mishka")
elif m < c:
    print("Chris")
else:
    print("Friendship is magic!^^")


# n = int(input())
# m = 0
# c = 0
# for _ in range(n):
#     x, y = list(map(int, input().split()))
#     if x > y:
#         m +=1
#     elif x < y:
#         c +=1
#
# if m > c:
#     print("Mishka")
# elif m < c:
#     print("Chris")
# else:
#     print("Friendship is magic!^^")