def base3(n):
    if(n==0):
        return
    x=n%3
    n//=3
    if(x<0):
        n+=1
    base3(n)
    if(x<0):
        print(x+(3*-1),end="")
    else:
        print(x,end="")
n=int(input())
print(base3(n))