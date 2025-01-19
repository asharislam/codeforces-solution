n = input()
total = 0
for i in n:
    if i =="4" or i =="7":
        total+=1
# print(total)
total = str(total)
if total =="4" or total=="7":
    print("YES")
else:
    print("NO")


#   Another way
# n = input()
# total = 0
# for i in n:
#     if i =="4" or i =="7":
#         total+=1
# total_s =str(total)
# is_lucky_count = True
#
# for j in total_s:
#     if j !="4" and j !="7":
#         is_lucky_count = False
#         break
#
# if is_lucky_count:
#     print("YES")
# else:
#     print("NO")