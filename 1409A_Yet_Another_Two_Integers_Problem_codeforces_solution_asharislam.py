# 1409A	Yet Another Two Integers Problem using python by Ashar Islam

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    c = abs(a-b)
    x = c//10
    if c%10 !=0:
        x +=1
    print(x)

# using while loop
# n = int(input())
# m = 0
# while m<n:
#     a, b = map(int, input().split())
#     c = abs(a-b)
#     x = c//10
#     if c%10 !=0:
#         x +=1
#     print(x)
#     m +=1