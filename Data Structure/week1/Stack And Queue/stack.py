#Creating a stack
def create_stack():
    stack=[]
    return stack

#Creating an empty stack
def check_empty(stack):
    return len(stack)==0

#Adding into the stack
def push(stack,value):
    stack.append(value)

#Return top of stack
def Top(stack):
    return stack[0]

#Remove a element of stack
def pop(stack):
    if (check_empty(stack)):
        return False
    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))