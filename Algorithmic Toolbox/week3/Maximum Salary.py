'''
To insert before a string: character_insert+string
To insert after a string:string+character_insert
'''

def Maximum_Salary(nums):
    max_salary=""
    if int(str(nums[1])+str(nums[0]))>int(str(nums[0])+str(nums[1])):
        max_salary+=str(nums[1])+str(nums[0])
    else:
        max_salary+=str(nums[0])+str(nums[1])
    for i in range(2,len(nums)):
        if int(str(nums[i])+max_salary)>int(max_salary+str(nums[i])):
            max_salary=str(nums[i])+max_salary
        else:
            max_salary=max_salary+str(nums[i])
    return max_salary
            


n=int(input())
number=list(map(int,input().split()))
number.sort()
if n==1:
    print(number[0])
else:
    print(Maximum_Salary(number))