# 581A	Vasya the Hipster using python by Ashar Islam

s = sorted(list(map(int, input().split())))
a = s[0]
b = s[1]

x = b-a
y = x//2
print(a)
print(y)


# Another way
a, b = sorted(list(map(int, input().split())))
x = b-a
y = x//2
print(a)
print(y)


# Another way
a, b = sorted(list(map(int, input().split())))
print(a)
print((b-a)//2)

# Another way
a, b = map(int, input().split())
x = min(a, b)
y = abs(a - b)
z = y//2
print(x)
print(z)
