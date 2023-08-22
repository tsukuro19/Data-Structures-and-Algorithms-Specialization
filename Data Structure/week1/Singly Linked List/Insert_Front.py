class Node:
    def __init__(self,data_val=None):
        self.data_val=data_val
        self.next_val=None

class SLinkedList:
    def __init__(self):
        self.head_val=None
        self.last_val=None
    def Push(self,data):
        if self.last_val is None:
            self.head_val=Node(data)
            self.last_val=self.head_val
        else:
            self.last_val.next_val=Node(data)
            self.last_val=self.last_val.next_val
    def Insert_Front(self,data):
        # 1 & 2: Allocate the Node &
        #        Put in the data
        new_node=Node(data)
        # 3. Make next of new Node as head
        new_node.next_val=self.head_val
        # 4. Move the head to point to new Node
        self.head_val=new_node
        if self.last_val is None:
            self.last_val=self.head_val
    def Print_SLinked_List(self):
        print_val=self.head_val
        while print_val is not None:
            print(print_val.data_val,end=' ')
            print_val=print_val.next_val


list1=SLinkedList()
n=int(input())
insert=int(input())
numbers=map(int,input().split(' '))
for i in numbers:
    list1.Push(i)
list1.Print_SLinked_List()
list1.Insert_Front(insert)
list1.Print_SLinked_List()