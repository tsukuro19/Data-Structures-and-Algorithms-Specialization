def GCD(a,b):
    if b==0:
        return a
    remainder=a%b
    return GCD(b,remainder)

def Least_Common_Multiple(a,b):
    return (a*b)/GCD(a,b)

a,b=map(int,input().split(' '))
print(int(Least_Common_Multiple(a,b)))