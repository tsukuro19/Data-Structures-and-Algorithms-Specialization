def Last_Digit_Sum_Of_Fibonacci_Square(n):
    previous=0
    current=1
    sum=1
    for i in range(n-1):
        previous, current = current, previous + current
        sum += current * current

    if n<=1:
        return n
    return sum


n=int(input())
print(Last_Digit_Sum_Of_Fibonacci_Square(n))