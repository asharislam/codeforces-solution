# 	151A - Soft Drinking using python by Ashar Islam

s = list(map(int, input().split()))

n = s[0]
k = s[1]
l = s[2]
c = s[3]
d = s[4]
p = s[5]
nl = s[6]
np = s[7]

kl = int((k*l)/nl)
cd = c*d
salt = int(p//np)

x = [kl, cd, salt]
print(min(x)//n)



# Another way to solve
# s = list(map(int, input().split()))
# n, k, l, c, d, p, nl, np = s
#
# total_drink = (k * l) // nl
# total_limes = c * d
# total_salt = p // np
#
# max_toasts = min(total_drink, total_limes, total_salt)
#
# print(max_toasts // n)
