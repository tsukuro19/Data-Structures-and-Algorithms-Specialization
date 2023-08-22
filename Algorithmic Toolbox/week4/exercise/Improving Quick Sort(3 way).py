#https://gist.github.com/adonese/4bf34d5b57ee0358626c
import random

def Particular3(a,l,r):
    lt=l
    gt=r
    i=l
    pivot=a[l]
    while i<=gt:
        if a[i]<pivot:
            a[lt],a[i]=a[i],a[lt]
            lt+=1
            i+=1
        elif a[i]>pivot:
            a[i],a[gt]=a[gt],a[i]
            gt-=1
        else:
            i+=1
    return lt,gt
    


def Improving_Quick_Sort(a,l,r):
    if l>=r:
        return a
    else:
        k=random.randint(l,r)
        a[l],a[k]=a[k],a[l]
        lt,gt=Particular3(a,l,r)
        Improving_Quick_Sort(a,l,lt-1)
        Improving_Quick_Sort(a,gt+1,r)
    return a

n=int(input())
a=list(map(int,input().split()))
pivot_r,pivot_l=len(a)-1,0
print(Improving_Quick_Sort(a,pivot_l,pivot_r))
