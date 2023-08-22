def Is_Balanced(str):
    stack=[]
    for i in range(0,len(str)):
        if str[i].isalpha()==True:
            continue
        else:
            if str[i] in ['(','[','{']:
                stack.append(str[i])
            else:
                if stack==[]:
                    return False
                top=stack.pop()
                if (top=='[' and str[i]!=']') or (top=='(' and str[i]!=')') or (top=='{' and str[i]!='}'):
                    return i+1
    return stack==[]

string=input()
if len(string)==1:
    print(1)
elif Is_Balanced(string)==True:
    print("Success")
else:
    print(Is_Balanced(string))