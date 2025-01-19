s = input()
t = input()
n = ""
for i, j in zip(s, t):
    if i == j:
     n +="0"
    else:
        n +="1"
print(n)