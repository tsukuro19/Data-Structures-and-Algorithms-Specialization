class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def Insert_Tree(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.Insert_Tree(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.Insert_Tree(data)
        else:
            self.data=data

    def Print_Tree(self):
        if self.left:
            self.left.Print_Tree()
        if self.right:
            self.right.Print_Tree()
        print(self.data,end=' ')


list_tree=list(map(int,input().strip().split()))
root=Node(list_tree[0])
#list_tree.remove(min(list_tree))
for i in range(1,len(list_tree)):
    root.Insert_Tree(list_tree[i])
root.Print_Tree()