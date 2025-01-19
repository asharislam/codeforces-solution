y = input()
z = int(y)

while 1000<=z:
    z +=1
    k = []
    for i in str(z):
        if i not in k:
            k.append(i)
    if len(k)==4:
        print(z)
        break


# Another way
# y = int(input())
# while 1000<=y:
#     y +=1
#     if len(set(str(y)))==4:
#         print(y)
#         break