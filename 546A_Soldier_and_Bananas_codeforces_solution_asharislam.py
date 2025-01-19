# Soldier and Bananas
x = input().split()
k = int(x[0])
n = int(x[1])
w = int(x[2])
total = 0
for i in range(1, w+1):
    total +=i*k
if total>n:
    print(total-n)
else:
    print(0)


# short solution
# x = input().split()
# total = 0
# for i in range(1, int(x[2])+1):
#     total +=i*int(x[0])
# if total>int(x[1]):
#     print(total-int(x[1]))
# else:
#     print(0)

# comprehension solution
# x = input().split()
# total = sum(i * int(x[0]) for i in range(1, int(x[2]) + 1))
# print(max(total - int(x[1]), 0))