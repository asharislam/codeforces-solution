# 9A	Die Roll using python by Ashar Islam

s = list(map(int, input().split()))
x = max(s)
successful_cases = 7 - x
total_cases = 6

a = successful_cases
b = total_cases

while b:
    a, b = b, a % b

print(str(successful_cases // a) + "/" + str(total_cases // a))
