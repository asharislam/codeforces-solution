# 1669A	Division? using python by Ashar Islam

n = int(input())
for _ in range(n):
    s = int(input())
    if 1900 <= s:
        print("Division 1")
    elif 1600<=s<=1899:
        print("Division 2")
    elif 1400<=s<=1599:
        print("Division 3")
    elif s<=1399:
        print("Division 4")
