n = int(input())
s = []
for i in range(1, n+1):
    if i%2==1:
        s.append("I")
        s.append("hate")
        s.append("that")
    elif i %2==0:
        s.append("I")
        s.append("love")
        s.append("that")
s[-1] = "it"
print(" ".join(s))