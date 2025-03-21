# 1472B	Fair Division using python by Ashar Islam

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    ones = s.count(1)
    twos = s.count(2)
    total = ones + 2 * twos

    if total % 2 != 0:
        print("NO")
        continue

    if ones > 0 or (twos % 2 == 0):
        print("YES")
    else:
        print("NO")
