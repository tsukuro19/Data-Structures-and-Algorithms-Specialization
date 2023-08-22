def Last_Digit_Sum_Of_Fibonacci(n):
    n_pisano=n%60
    F=[]
    sum=1
    F.append(0)
    F.append(1)
    for i in range(2,n_pisano+1):
        F.append(F[i-1]+F[i-2])
        sum+=F[i]
    string_change=str(sum)
    return string_change[len(string_change)-1]

n=int(input())
print(int(Last_Digit_Sum_Of_Fibonacci(n)))