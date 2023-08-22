def EuclidGCD(a,b):
    if b==0:
        return a
    a1=a%b
    return EuclidGCD(b,a1)

a,b=map(int,input().split(' '))
print(EuclidGCD(a,b))