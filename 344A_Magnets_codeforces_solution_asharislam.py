n = int(input())
k = ""

for i in range(n):
    x = input()
    if x =="10":
        k +="A"
    else:
        k +="S"
m = k[0]
for i in range(1, len(k)):
    if k[i] != k[i-1]:
        m +=k[i]
print(len(m))


# Another way
# n = int(input())
# total = 0
# y = 0
# for _ in range(n):
#     x = input().strip()
#     if x != y:
#         total +=1
#         y = x
# print(total)