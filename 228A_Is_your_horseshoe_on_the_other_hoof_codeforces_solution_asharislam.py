n = input().split()
s = []
for i in n:
    if i not in s:
        s.append(i)
print(4- len(s))


# Another way
# n = input().split()
# s = list(set(n))
# print(4-len(s))

# Another way
# s = list(set(input().split()))
# print(4-len(s))