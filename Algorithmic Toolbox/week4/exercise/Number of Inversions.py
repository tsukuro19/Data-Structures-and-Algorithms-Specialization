def Merge_Sort(a,tmp,left,right):
    inv=0
    if left<right:
        mid=(left+right)//2
        inv+=Merge_Sort(a,tmp,left,mid)
        inv+=Merge_Sort(a,tmp,mid+1,right)
        inv+=Merge(a,tmp,left,mid,right)
    return inv

def Merge(a,tmp,left,mid,right):
    i,j,inv,k=left,mid+1,0,left
    while i<=mid and j<=right:
        if a[i]<=a[j]:
            tmp[k]=a[i]
            i+=1
            k+=1
        else:
            tmp[k]=a[j]
            inv+=mid-i+1
            k+=1
            j+=1
    while i<=mid:
        tmp[k]=a[i]
        k+=1
        i+=1
    while j<=right:
        tmp[k]=a[j]
        k+=1
        j+=1
    for i in range(left,right+1):
        a[i]=tmp[i]
    return inv

n=int(input())
tmp=[0]*n
a=list(map(int,input().split()))
print(Merge_Sort(a,tmp,0,n-1))