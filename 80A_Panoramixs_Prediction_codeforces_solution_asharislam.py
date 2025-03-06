# 80A	Panoramix's Prediction using python by Ashar Islam

n, m = map(int, input().split())
next_prime = -1

for num in range(n + 1, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        next_prime = num
        break

if next_prime == m:
    print("YES")
else:
    print("NO")




























































