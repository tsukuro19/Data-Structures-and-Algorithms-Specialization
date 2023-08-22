def Majority_Element_Naive(a,n):
    temp=0
    for i in range(n):
        current_element=a[i]
        count=0
        for j in range(n):
            if a[j]==current_element:
                count+=1
        if count>(n/2):
            temp=a[i]
            print(temp)
            break
    if temp==0:
        print('no majority element')
n=int(input())
a=list(map(int,input().split()))
Majority_Element_Naive(a,n)