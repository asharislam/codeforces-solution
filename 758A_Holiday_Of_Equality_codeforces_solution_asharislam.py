# 758A	Holiday Of Equality using python by Ashar Islam

n = input()
s = list(map(int, input().split()))
x = max(s)
total = 0

for i in s:
     if i <x:
         total +=x - i
print(total)

# n = input()
# s = list(map(int, input().split()))
# total = 0
#
# for i in s:
#      if i <max(s):
#          total +=max(s) - i
# print(total)

# n = input()
# s = list(map(int, input().split()))
#
# x = max(s)
# total = sum(x - i for i in s)
# print(total)
