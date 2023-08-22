def Money_Change(money):
    number_coins=0
    denominations=[1,5,10]
    while money!=0:
        if money>=max(denominations):
            money-=max(denominations)
            number_coins+=1
        else:
            denominations.remove(max(denominations))
    return number_coins

money=int(input())
print(Money_Change(money))