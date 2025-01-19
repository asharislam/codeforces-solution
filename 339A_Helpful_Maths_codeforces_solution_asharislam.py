

s = input()
s = sorted(s)
total = ""
for i in s:
    if i == "+":
        pass
    else:
        total+=str(i+"+")
total = total[:-1]
print(total)

# Another way
# s =input().split("+")
# x = "+".join(sorted(s))
# print(x)