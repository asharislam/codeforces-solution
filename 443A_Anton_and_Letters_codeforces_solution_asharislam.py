# 443A - Anton and Letters using python by Ashar Islam

x = input()
y = x[1:-1].split(", ")

if y !=[""]:
    print(len(set(y)))
else:
    print(0)


# Another way(comprehension way)
# x = input()
# y = x[1:-1].split(", ")
# print(len(set(y)) if y !=[""] else 0)