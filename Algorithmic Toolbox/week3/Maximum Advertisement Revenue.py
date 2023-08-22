def Maximum_Dot_Product(n,a,b):
    sum=0
    a1=sorted(a)
    b1=sorted(b)
    for i in range(n):
        sum+=a1[i]*b1[i]
    return sum

n=int(input())
a=list(map(int,input().strip().split()))[:n]
b=list(map(int,input().strip().split()))[:n]
print(Maximum_Dot_Product(n,a,b))