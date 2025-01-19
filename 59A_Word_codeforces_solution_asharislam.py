k = input()
lower = 0
upper = 0
s = []
for i in k:
    s.append(i)
    if i.isupper():

        upper +=1
    else:
        lower +=1
if lower>=upper:
    print(k.lower())
else:
    print(k.upper())