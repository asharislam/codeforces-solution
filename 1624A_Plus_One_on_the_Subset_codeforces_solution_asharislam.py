# 1624A	Plus One on the Subset using python by Ashar Islam

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if n == 5 and sorted(s) == sorted("Timur"):
        print("YES")
    else:
        print("NO")
