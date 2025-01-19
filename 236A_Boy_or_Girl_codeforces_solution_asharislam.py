x = input()
y =[]
# print(x)
for i in x:
    y.append(i)
y = list(dict.fromkeys(y))
if len(y)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

#   Another way
# x = input()
# y =""
# for i in x:
#     if i not in y:
#         y+=i
# if len(y)%2==0:
#     print("CHAT WITH HER!")
# else:
#     print("IGNORE HIM!")

#   Another way
# x = input()
# x = dict.fromkeys(x)
# if len(x)%2==0:
#     print("CHAT WITH HER!")
# else:
#     print("IGNORE HIM!")