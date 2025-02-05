# 381A	Sereja and Dima using python by Ashar Islam

n = int(input())
s= list(map(int, input().split()))
x = 0
y = 0
turn = True

for _ in range(n):
    if s[0] > s[-1]:
        z = s.pop(0)
    else:
        z = s.pop()
    if turn:
        x +=z
    else:
        y +=z
    turn = not turn
print(x, y)



# Another day
# n = int(input())
# s = list(map(int, input().split()))
# x = 0
# y = 0
# turn = True
#
# while s:
#     if s[0] > s[-1]:
#         z = s.pop(0)
#     else:
#         z = s.pop()
#
    # if turn:
    #     x +=z
    # else:
    #     y +=z
    # turn = not turn
# print(x, y)


# comprehension
# n = int(input())
# s = list(map(int, input().split()))
# x = 0
# y = 0
# turn = True
#
# while s:
#     z = s.pop(0) if s[0] > s[-1] else s.pop()
#     x, y = (x + z, y) if turn else (x, y + z)
#     turn = not turn
#
# print(x, y)


# comprehension
# n = int(input())
# s = list(map(int, input().split()))
#
# x, y, turn = 0, 0, True
# for z in [s.pop(0) if s[0] > s[-1] else s.pop() for _ in range(n)]:
#     if turn:
#         x += z
#     else:
#         y += z
#     turn = not turn
#
# print(x, y)

