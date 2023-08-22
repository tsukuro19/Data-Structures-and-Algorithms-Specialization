def Find_First_Index(a,key,high,low):
    if a[low]==key:
        return low
    if high==low:
        return -1
    mid=low+(high-low)//2
    if a[mid]==key:
        return Find_First_Index(a,key,mid,low)
    return Find_First_Index(a,key,high,mid+1)

    
def Find_Last_Index(a,key,high,low):
    if high<low:
        return -1
    mid=low+(high-low)//2
    if key==a[mid]:
        return mid
    if key>a[mid]:
        return Find_Last_Index(a,key,high,mid+1)
    else:
        return Find_Last_Index(a,key,mid-1,low)

def Majority_Element(a):
    mid=0+int(((len(a)-1)-0)/2)
    temp=0
    fist_half=[a[0:mid]]
    last_half=[a[mid:len(a)]]
    low,high=0,len(last_half)-1
    for i in range(len(fist_half)):
        if Find_Last_Index(last_half,fist_half[i],high,low)==-1:
            continue
        else:
            if temp>(Find_Last_Index(last_half,fist_half[i],high,low)-Find_First_Index(last_half,fist_half[i],high,low)):
                temp=Find_Last_Index(last_half,fist_half[i],high,low)-Find_First_Index(last_half,fist_half[i],high,low)
    if temp>(len(a)/2):
        print(1)
    else:
        print(0)


n=int(input())
a=list(map(int,input().split()))
a_sorted=sorted(a)
Majority_Element(a_sorted)
