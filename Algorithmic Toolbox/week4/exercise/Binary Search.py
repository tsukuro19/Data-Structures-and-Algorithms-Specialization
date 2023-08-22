def Binary_Search(l,key,low,high):
    mid=low+(high-low)//2
    if high<low:
        return -1
    mid=low+(high-low)//2
    if l[mid]==key:
        return mid
    elif l[mid]>key:
        return Binary_Search(l,key,0,mid-1)
    else:
        return Binary_Search(l,key,mid+1,high)


number_contain=int(input())
list_contain=list(map(int,input().split()))
number_check=int(input())
list_check=list(map(int,input().split()))
for i in range(number_check):
    print(Binary_Search(list_contain,list_check[i],0,number_contain-1),end=" ")