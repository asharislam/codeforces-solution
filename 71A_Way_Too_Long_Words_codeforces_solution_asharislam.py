# way too land words using python by Ashar Islam
n = int(input())
for i in range(n):
    x = input("")
    y = len(x)
    if y > 10:
        print(f"{x[0]}{len(x) - 2}{x[-1]}")
    else:
        print(x)