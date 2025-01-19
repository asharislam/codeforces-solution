n = int(input())
x = input().split()
y = input().split()
z = list(set(x[1:]+y[1:])-{"0"})
# print(z)
if len(z) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")