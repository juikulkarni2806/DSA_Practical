#BST using Linked List
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None
        self.cnt=0
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
            if rt.left is None and rt.right is None:
                self.cnt+=1
            print(rt.data, end=" ")
            self.inorder(rt.right)

    def preorder(self,rt):
        
        if rt is None:
            return
        else:
            
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)
    
    def postorder(self,rt):
        
        if rt is None:
            return
        else:
            
           
            self.preorder(rt.left)
            self.preorder(rt.right)
            print(rt.data, end=" ")

    def findminmax(self,rt):
        temp=rt
        while temp.left:
            temp=temp.left
        print("\nMin: ",temp.data)
        temp=self.root
        while temp.right:
            temp=temp.right
        print("\nMax: ",temp.data)

    def del_node(self,rt,val):
        if rt is None:
            return rt
        if val<rt.data:
            rt.left=self.del_node(rt.left,val)

        elif val>rt.data:
            rt.right=self.del_node(rt.right,val)

        else:
            if rt.left is None:
                return rt.right
            if rt.right is None:
                return rt.left
        #when node has both left and right child.
        
        succ=self.get_successor(rt)
        rt.data=succ.data
        rt.right=self.del_node(rt.right,succ.data)
        return rt
    def get_successor(self,temp):
        temp=temp.right
        while temp is not None and temp.left is not None:
            temp=temp.left
        return temp 
    def search(self,key):
        temp=self.root
        while temp:
            if temp.data==key:
                return True
            elif key<temp.data:
                temp=temp.left
            else:
                temp=temp.right
        return False




    


b1=BST()
b1.insert(Node(11))
b1.insert(Node(1))
b1.insert(Node(45))
b1.insert(Node(24))
b1.insert(Node(105))
b1.insert(Node(30))
b1.insert(Node(15))
print("Inorder:")
b1.inorder(b1.root)
print("\nPreorder:")
b1.preorder(b1.root)
print("\nPostorder:")
b1.postorder(b1.root)
b1.findminmax(b1.root)
# b1.root = b1.del_node(b1.root, 45)
# print("After Delete:")
# b1.inorder(b1.root)
if b1.search(243):
    print("\n Found The Node.")
else:
    print("\nNot Found")
b1.search(1232)
print(b1.cnt)




