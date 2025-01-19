# Next Round using python by Ashar Islam
k = int(input().split()[1])
score = input().split()
total = 0
for i in score:
    if int(i)>0:
        if int(i)>=int(score[k-1]):
            total+=1
print(total)


# Another way
# k = int(input().split()[1])
# score = input().split()
# total = 0
# for i in score:
#     if int(i)>0 and int(i)>=int(score[k-1]):
#         total+=1
# print(total)