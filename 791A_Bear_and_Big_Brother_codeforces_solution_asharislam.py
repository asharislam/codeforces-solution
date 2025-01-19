a = input().split()
b = []
for i in a:
    b.append(int(i))
total = 0
x = b[0]
y = b[1]
while x<=y:
    x *= 3
    y *= 2
    total +=1
print(total)


# Another way
# b =[int(i) for i in input().split()]
# x = b[0]
# y = b[1]
# total = 0
# while x <=y:
#     x *= 3
#     y *= 2
#     total +=1
# print(total)