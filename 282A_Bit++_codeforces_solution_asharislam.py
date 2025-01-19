# Bit++ using python by Ashar Islam


x = 0
n =int(input())
for i in range(n):
    user = input()
    if '+' in user:
        x+=1
    else:
        x-=1
print(x)


# Another Way
# x = 0
# n =int(input())
# for _ in range(n):
#     if '+' in input():
#         x+=1
#     else:
#         x-=1
# print(x)


# Another way
# x = 0
# for _ in range(int(input())):
#     x = x + 1 if '+' in input() else x - 1
# print(x)