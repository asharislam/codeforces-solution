# 732A	Buy a Shovel using python by Ashar Islam

s = list(map(int, input().split()))
k = s[0]
r = s[1]

m =0
while True:
    m +=1
    total = m *k
    if total % 10 ==0 or total % 10 ==r:
        print(m)
        break


# Another way to solve
# s = list(map(int, input().split()))
# k = s[0]
# r = s[1]
#
# for i in range(1, 11):
#     total = i *k
#     if total % 10 ==0 or total % 10 ==r:
#         print(i)
#         break