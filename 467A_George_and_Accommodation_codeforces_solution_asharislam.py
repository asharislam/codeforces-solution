n = int(input())
total = 0
for i in range(n):
    x = input().split()
    if int(x[0])+2 <= int(x[1]):
        total +=1
print(total)