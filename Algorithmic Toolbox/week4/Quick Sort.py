def Partition(a,l,r):
    # Last element will be the pivot and the first element the pointer
    x=a[r]
    j=l
    for i in range(l,r):
        if a[i]<=x:
            # Swapping values smaller than the pivot to the front
            a[j],a[i]=a[i],a[j]
            j=j+1
    # Finally swapping the last element with the pointer indexed number
    a[j],a[r]=a[r],a[j]
    return j

def Quick_Sort(a,l,r):
    if l>=r:
        return a
    else:
        m=Partition(a,l,r)
        Quick_Sort(a,m+1,r)
        Quick_Sort(a,l,m-1)
    return a

a=list(map(int,input().split()))
pivot_l=0
pivot_r=len(a)-1
print(Quick_Sort(a,pivot_l,pivot_r))