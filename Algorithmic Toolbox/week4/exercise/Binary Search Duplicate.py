def Find_Star_Index(a,key,low,high):
    start_index=-1
    while(low<=high):
        mid=low+(high-low)//2
        if key==a[mid]:
            start_index=mid
            high=mid-1
        elif key<a[mid]:
            high=mid-1
        else:
            low=mid+1
    return start_index

def Find_End_Index(a,key,low,high):
    end_index=-1
    while(low<=high):
        mid=low+(high-low)//2
        if key==a[mid]:
            end_index=mid
            low=mid+1
        elif key<a[mid]:
            high=mid-1
        else:
            low=mid+1
    return end_index

number_contain=int(input())
list_contain=list(map(int,input().split()))
number_check=int(input())
list_check=list(map(int,input().split()))
result=[]
for i in range(number_check):
    start_key=Find_Star_Index(list_contain,list_check[i],0,number_contain-1)
    end_key=Find_End_Index(list_contain,list_check[i],0,number_contain-1)
    if start_key==-1 and end_key==-1:
        result.append(-1)
    else:
        if start_key==end_key:
            result.append(start_key)
        else:
            if start_key==-1:
                result.append(end_key)
            else:
                result.append(start_key)
print(' '.join(map(str,result)))