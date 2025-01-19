# A Team using python by Ashar Islam
n = int(input())
total = 0
for i in range(n):
    user = input()
    x = user.count("1")
    if x >=2:
        total+=1
print(total)