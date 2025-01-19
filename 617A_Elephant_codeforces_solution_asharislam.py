x = int(input())
y = x//5
if x%5>0:
    z = 1
else:
    z =0
total = y + z
print(total)


# Another way
# x = int(input())
# y = x//5
# if x%5>0:
#     y +=1
# else:
#     pass
# print(y)

# Another way
# x = int(input())
# print(x // 5 + (1 if x % 5 > 0 else 0))