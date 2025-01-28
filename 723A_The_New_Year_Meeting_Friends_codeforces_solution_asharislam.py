# 723A	The New Year: Meeting Friends using python by Ashar Islam

# s = list(map(int, input().split()))
# x1 = [abs(s[0]-s[1]), abs(s[1]-s[2]), abs(s[0]-s[2])]
# x1.remove(max(x1))
# print(sum(x1))


# Another way to solve
s = sorted(map(int, input().split()))
print(abs(s[1] - s[0]) + abs(s[2] - s[1]))
