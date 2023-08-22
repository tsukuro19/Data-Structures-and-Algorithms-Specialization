def Last_Digit_Of_Sum_Fibonacci_Again(m,n):
    m_pisano=m%60
    n_pisano=n%60
    sum=0
    current=0
    next=1
    if n_pisano<m_pisano:
        n_pisano+=60
    for i in range(n_pisano+1):
        if i>=m_pisano:
            sum+=current
        new_current=next
        next=next+current
        current=new_current
    str_change=str(sum)
    return str_change[len(str_change)-1]


m,n=map(int,input().split())
print(Last_Digit_Of_Sum_Fibonacci_Again(m,n))