def Refill(Stops,m,n,d):
    current=0
    count=0
    if d<=m:
        return count
    else:
        while current<n:
            last=current
            while current<=n-1:
                if Stops[last]-Stops[current+1]<=m:
                    current+=1
                else:
                    break
            if last==current:
                return -1
            if current<=n:
                count+=1
        return count
        

d=int(input())
m=int(input())
n=int(input())
Stops=list(map(int,input().strip().split()))+[d]
Stops.sort(reverse=True)
print(Refill(Stops,m,n,d))
