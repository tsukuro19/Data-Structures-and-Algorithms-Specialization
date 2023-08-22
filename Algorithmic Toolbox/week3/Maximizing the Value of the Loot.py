'''The code c = input() reads a string from the user and assigns it to the variable c.
The code n, capacity = map(int, c.split()) splits the string c on spaces and converts the resulting list of strings to a list of integers
The first element in the list of integers is assigned to the variable n, and the second element is assigned to the variable capacity.'''


def Maximum_value(capacity,ratio,dic):
    v=0
    for i in range(n):
        if capacity==0:
            return v
        else:
            res=min(capacity,dic[ratio[i]])
            v+=ratio[i]*res
            capacity-=res
    return v

c = input()
n, capacity = map(int, c.split())
dic={}
ratio=[]
for i in range(n):
    v,w=map(int,input().split())
    ratio.append(v/w)
    dic[v/w]=w
ratio.sort(reverse=True)
result=Maximum_value(capacity,ratio,dic)
print("{:.4f}".format(result))