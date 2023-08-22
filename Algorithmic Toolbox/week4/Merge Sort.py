def Merge(b,c):
    d=[]
    i=j=0
    while i<len(b) and j<len(c):
        if b[i]<=c[j]:
            d.append(b[i])
            i+=1
        else:
            d.append(c[j])
            j+=1
    while i<len(b):
        d.append(b[i])
        i+=1
    while j<len(c):
        d.append(c[j])
        j+=1
    return d

def Merge_Sort(a):
    n=len(a)
    if n==1:
        return a
    m=int(n/2)
    b=Merge_Sort(a[:m])
    c=Merge_Sort(a[m:])
    a1=Merge(b,c)
    return a1        


a=list(map(int,input().split()))
print(Merge_Sort(a))