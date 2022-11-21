n=int(input())
l=['0','1','2','5','6','8','9']
x=len(l)
i=0
s=""
while n>0:
    s=s+l[n%x]
    n//=x
s=s[::-1]
print(int(s))


