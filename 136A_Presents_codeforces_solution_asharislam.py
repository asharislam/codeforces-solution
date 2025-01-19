n = int(input())
s = input().split()
t = [0]*n

for i in range(n):
    x = int(s[i])
    t[x - 1] = i +1

total = ""
for j in t:
    total += str(j) + " "
print(total)