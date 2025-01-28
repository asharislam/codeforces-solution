# 427A	Police Recruits using python by Ashar Islam

n = int(input())
s = list(map(int, input().split()))

x = 0
y = 0

for i in s:
    if i == -1:
        if x >0:
            x -=1
        else:
            y +=1
    else:
        x += i
print(y)


# Details to understand
# n = int(input())
# s = list(map(int, input().split()))
#
# available_officers = 0
# untreated_crimes = 0
#
# for i in s:
#     if i == -1:
#         if available_officers > 0:
#             available_officers -= 1
#         else:
#             untreated_crimes += 1
#     else:
#         available_officers += i
#
# print(untreated_crimes)