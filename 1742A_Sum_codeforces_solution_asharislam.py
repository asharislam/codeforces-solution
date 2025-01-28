# 1742A	Sum using python by Ashar Islam

n = int(input())
for _ in range(n):
    s = list(map(int, input().split()))
    if s[0] + s[1] == s[2] or s[1] + s[2] == s[0] or s[0]+s[2]==s[1]:
        print("YES")
    else:
        print("NO")
