import sys

def Cat_And_Mouse(x,y,z):
    if abs(z-x)==abs(z-y):
        return 'Mouse C'
    else:
        if abs(z-x)>abs(z-y):
            return 'Cat B'
        else:
            return 'Cat A'


if __name__=='__main__':
    q = int(input().strip())
    for a0 in range(q):
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = Cat_And_Mouse(x, y, z)
        print ("".join(map(str, result)))

