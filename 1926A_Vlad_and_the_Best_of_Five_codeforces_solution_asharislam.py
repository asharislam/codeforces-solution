# 1926A	Vlad and the Best of Five using python by Ashar Islam

# n = int(input())
# for _ in range(n):
#     s = input()
#     a = s.count("A")
#     b = s.count("B")
#
#     if a > b:
#         print("A")
#     else:
#         print("B")


n = int(input())
for _ in range(n):
    s = input()

    if s.count("A") > s.count("B"):
        print("A")
    else:
        print("B")