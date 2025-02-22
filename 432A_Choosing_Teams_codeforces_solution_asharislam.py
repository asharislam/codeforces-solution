# 432A	Choosing Teams using python by Ashar Islam

n, k = map(int, input().split())
s = list(map(int, input().split()))
total = 0

for i in s:
    if i+k <= 5:
        total +=1
print(total//3)
