n = int(input())
s = list(map(int, input().split()))

max_s = max(s)
min_s = min(s)
max_i = s.index(max_s)
min_i = len(s) - 1 - s[::-1].index(min_s)

if max_i > min_i:
    swaps = max_i + (n - 1 - min_i) - 1
else:
    swaps = max_i + (n - 1 - min_i)
print(swaps)