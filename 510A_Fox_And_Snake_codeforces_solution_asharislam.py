# 510A - Fox And Snake using python by Ashar Islam

m = list(map(int, input().split()))
n = m[0]
s = m[1]

for i in range(1, n+1):
    if i%2==1:
        print("#"*s)
    elif i%4==0:
        x = ["."] * s
        x[0] = "#"
        print("".join(x))
    else:
        x = ["."] * s
        x[-1] = "#"
        print("".join(x))



# Another condition
# m = list(map(int, input().split()))
# n = m[0]
# s = m[1]
#
# for i in range(1, n+1):
#     if i%4==0:
#         x = ["."] * s
#         x[0] = "#"
#         print("".join(x))
#     elif i%2==0:
#         x = ["."] * s
#         x[-1] = "#"
#         print("".join(x))
#     else:
#         print("#" * s)


