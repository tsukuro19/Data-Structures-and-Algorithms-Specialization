def NaiveGCD(a,b):
    best=0
    for d in range(1,a+b):
        if a%d==0 and b%d==0:
            best=d
    return best

a,b=map(int,input().split(' '))
print(NaiveGCD(a,b))