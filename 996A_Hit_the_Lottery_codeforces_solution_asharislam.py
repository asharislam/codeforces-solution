# 996A - Hit the Lottery - using python by Ashar Islam

n = int(input())
total = 0
s = [100, 20, 10, 5, 1]

for i in s:
    if i<=n:
        total += n//i
        n = n%i
print(total)