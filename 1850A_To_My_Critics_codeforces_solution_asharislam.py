# 1850A	To My Critics using python by Ashar Islam

n = int(input())
for _ in range(n):
    s = list(map(int, input().split()))
    if s[0] + s[1] >=10 or s[0] + s[2] >=10 or s[1] + s[2]>=10:
        print("YES")
    else:
        print("NO")


# n = int(input())
# for _ in range(n):
#     a, b, c = map(int, input().split())
#     print("YES" if any(x + y >= 10 for x, y in [(a, b), (a, c), (b, c)]) else "NO")
