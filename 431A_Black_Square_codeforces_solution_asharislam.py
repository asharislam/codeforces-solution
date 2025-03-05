# 431A	Black Square using python by Ashar Islam

s = list(map(int, input().split()))
n = input().strip()
total = 0
for i in n:
    total +=s[int(i) - 1]
print(total)


# a = list(map(int, input().split()))
# s = input().strip()
# calories = {'1': a[0], '2': a[1], '3': a[2], '4': a[3]}
# total_calories = sum(calories[c] for c in s)
# print(total_calories)
