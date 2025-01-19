n = input()
s = input().lower()
t =""
for i in s:
    if i not in t:
        t +=i
if len(t) == 26:
    print("YES")
else:
    print("NO")


# Another way
# n = input()
# s = set(input().lower())
# if len(s) == 26:
#     print("YES")
# else:
#     print("NO")
