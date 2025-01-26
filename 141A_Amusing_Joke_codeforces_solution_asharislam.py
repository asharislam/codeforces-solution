# 141A_Amusing_Joke using python by Ashar Islam

x = input()
y = input()
z = input()
k = x + y

k_count = {}
for i in k:
    k_count[i] = k_count.get(i, 0) + 1

z_count = {}
for j in z:
    z_count[j] = z_count.get(j, 0) + 1

if k_count == z_count:
    print("YES")
else:
    print("NO")


# Another way to solve using library
# from collections import Counter
#
# x = input()
# y = input()
# z = input()
# k = x + y
#
# if Counter(k) == Counter(z):
#     print("YES")
# else:
#     print("NO")