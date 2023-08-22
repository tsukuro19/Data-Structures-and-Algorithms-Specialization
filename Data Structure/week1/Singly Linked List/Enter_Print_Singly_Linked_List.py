class Node:
    def __init__(self,data_val=None):
        self.data_val=data_val
        self.next_val=None
    
class SLinkedList:
    def __init__(self):
        self.head_val=None
        self.last_val=None
    def push(self,data):
        if self.last_val is None:
            self.head_val=Node(data)
            self.last_val=self.head_val
        else:
            self.last_val.next_val=Node(data)
            self.last_val=self.last_val.next_val
    def list_print(self):
        print_val=self.head_val
        while print_val is not None:
            print(print_val.data_val,end=' ')
            print_val=print_val.next_val

list1=SLinkedList()
n=int(input())
numbers=map(int,input().split(' '))
for i in numbers:
    list1.push(i)
list1.list_print()