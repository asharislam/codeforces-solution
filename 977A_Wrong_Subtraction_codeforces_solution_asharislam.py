x = input().split()
n = int(x[0])
k = int(x[1])
for i in range(1, k+1):
    if int(str(n)[-1]) !=0:
        n -=1
    else:
        n = int(str(n)[:-1])
print(n)