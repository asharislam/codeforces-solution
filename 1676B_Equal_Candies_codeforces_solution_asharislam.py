# 1676B	Equal Candies using python by Ashar Islam

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    x = sum(s)- min(s)*n
    print(x)

