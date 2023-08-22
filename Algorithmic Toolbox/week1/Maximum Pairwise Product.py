n=int(input())
a=[int(i) for i in input().split()]

x1=max(a)
a.remove(x1)
x2=max(a)
print(x1*x2)