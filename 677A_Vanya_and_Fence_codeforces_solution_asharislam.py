m = input().split()
n = int(m[0])
h = int(m[1])
total = 0
x = input().split()
for i in range(n):
    if int(x[i])<=h:
        total +=1
    else:
        total +=2
print(total)


# Another way
# m = input().split()
# x = input().split()
# total = 0
#
# for i in range(int(m[0])):
#     if int(x[i])<=int(m[1]):
#         total +=1
#     else:
#         total +=2
# print(total)