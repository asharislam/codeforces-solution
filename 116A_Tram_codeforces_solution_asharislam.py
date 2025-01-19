n = int(input())
total = 0
maximum = 0

for i in range(n):
    user = input().split()
    x = int(user[0])
    y = int(user[1])

    total -=x
    total +=y
    if total>maximum:
        maximum = total
print(maximum)

