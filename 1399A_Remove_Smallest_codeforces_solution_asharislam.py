# 1399A - Remove Smallest using python by Ashar Islam

t = int(input())
for _ in range(t):
    n = int(input())
    s = sorted(list(map(int, input().split())))
    x = True
    for i in range(n-1):
        if abs(s[i]-s[i+1]) >1:
            x = False
            break
    if x:
        print("YES")
    else:
        print("NO")