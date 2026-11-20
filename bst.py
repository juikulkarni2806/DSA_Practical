#BST using Linked List
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,new_node):
        if self.root is None:
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else:
                     
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right

    def inorder(self,rt):
        
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.inorder(rt.right)

    def preorder(self,rt):
        
        if rt is None:
            return
        else:
            
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

b1=BST()
b1.insert(Node(110))
b1.insert(Node(10))
b1.insert(Node(45))
b1.insert(Node(6))
b1.insert(Node(650))
b1.insert(Node(30))
b1.insert(Node(15))
print("Inorder:")
b1.inorder(b1.root)
print("\nPreorder:")
b1.preorder(b1.root)



