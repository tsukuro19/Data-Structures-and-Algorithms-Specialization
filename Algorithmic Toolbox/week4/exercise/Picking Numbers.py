import sys    

def Picking(a):
    keys=list(set(a))
    dict_a={k:0 for k in keys}
    for el in a:
        dict_a[el]+=1
    lengths=[dict_a[a]+dict_a[b] if b-a==1 else max(dict_a[a],dict_a[b]) for a,b in 
             zip(keys[:-1],keys[1:])]
    return max(lengths) if len(keys)>1 else len(a)


if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    print(Picking(sorted(arr)))