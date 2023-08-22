def collect(seg):
    current=0
    ends=[]
    while current<n:
        last=current
        while current<n-1 and seg[current+1][0]<=seg[last][1]:
            current+=1
            if seg[current][1]<seg[last][1]:
                last=current
        current+=1
        ends.append(seg[last][1])
    return ends


n=int(input())
seg=[]
for i in range(n):
    seg.append(list(map(int,input().split())))
seg.sort()
print(len(collect(seg)))
for end in collect(seg):
    print(end,end=' ')
    