# 1950A	Stair, Peak, or Neither? using python by Ashar Islam

n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    if a < b < c:
        print("STAIR")
    elif a < b > c:
        print("PEAK")
    else:
        print("NONE")


# n = int(input())
# for _ in range(n):
#     a, b, c = map(int, input().split())
#     if a < b and b < c:
#         print("STAIR")
#     elif a < b and b > c:
#         print("PEAK")
#     else:
#         print("NONE")


# n = int(input())
# for _ in range(n):
#     a, b, c = map(int, input().split())
#     print("STAIR" if a < b < c else "PEAK" if a < b > c else "NONE")
