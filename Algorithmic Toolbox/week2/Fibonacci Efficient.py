def FibList(n):
    F=[int (i) for i in range(0,n+1)]
    F[0]=1
    F[1]=1
    for i in range(2,n+1):
        F[i]=F[i-1]+F[i-2]
    return F[n]

n=int(input())
if n==0:
    print(1)
else:
    print(FibList(n))