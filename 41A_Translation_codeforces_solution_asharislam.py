# 41A_Translation_codeforces_solution_asharislam
s = input()
t = input()
y = s[::-1]
if t ==y:
    print("YES")
else:
    print("NO")


#   Another way
# s = input()[::-1]
# t = input()
# if s ==t:
#     print("YES")
# else:
#     print("NO")

#   Another way
# s = input()[::-1]
# t = input()
# print("YES" if s==t else "NO")


# Another way
# print("YES" if input()==input()[::-1] else "NO")
