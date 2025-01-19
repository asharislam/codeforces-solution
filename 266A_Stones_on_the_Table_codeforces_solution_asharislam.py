m = input()
s = input()
count = 0
n =[i for i in range(0, int(m))]
for j in n:
    if j<len(n)-1:
        if s[j] == s[j+1]:
            count+=1
print(count)