def Maximum_Number_Of_Prizes(n):
    i=0
    prize=[]
    while n>0:
        i+=1
        if n-i<i+1:
            i=n
        prize.append(i)
        n-=i
    return prize


n=int(input())
print(Maximum_Number_Of_Prizes(n))