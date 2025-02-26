# 1367A	Short Substrings using python by Ashar Islam

n =  int(input())
for _ in range(n):
    s = input().strip()
    x = s[0]
    for i in range(1, len(s), 2):
        x +=s[i]
    print(x)
