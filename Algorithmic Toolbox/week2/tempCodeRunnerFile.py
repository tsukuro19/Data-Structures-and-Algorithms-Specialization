def FibList(n):
    F=[]
    F.append(0)
    F.append(1)
    for i in range(2,n+1):
        F.append(F[i-1]+F[i-2])
    return F[n]%10

n=int(input())
print(FibList(n))