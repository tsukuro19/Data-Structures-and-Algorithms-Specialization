def Get_Money(keyboard,drives,b):
    max_bill=-1
    keyboard.sort()
    drives=sorted(drives,reverse=True)
    for k in keyboard:
        while len(drives)!=0 and k+drives[0]>b:
            drives.pop(0)
        if len(drives)!=0 and (max_bill<k+drives[0]<=b):
            max_bill=k+drives[0]
    return max_bill


b,n,m=map(int,input().split(' '))
keyboard=list(map(int,input().split()))
drives=list(map(int,input().split()))
print(Get_Money(keyboard,drives,b))