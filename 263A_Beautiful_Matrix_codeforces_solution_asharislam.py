a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
d = [int(i) for i in input().split()]
e = [int(i) for i in input().split()]

cm = 3
rm = 3
if sum(a) != 0:
    row = 1
    column = a.index(1) + 1
elif sum(b) != 0:
    row = 2
    column = b.index(1) + 1
elif sum(c) != 0:
    row = 3
    column = c.index(1) + 1
elif sum(d) != 0:
    row = 4
    column = d.index(1) + 1
else:
    row = 5
    column = e.index(1) + 1
print(abs(column - cm) + abs(rm - row))