class Node:
    def __init__(s,data,left=None,right=None):
        s.data=data
        s.left=left
        s.right=right
    def inorder(s,root):
        if(root):
            s.inorder(root.left)
            print(root.data,end=" --> ")
            s.inorder(root.right)
    def preorder(s,root): 
        if(root):
            print(root.data,end=" --> ")
            s.preorder(root.left)
            s.preorder(root.right)
    def postorder(s,root):
        if(root):
            s.postorder(root.left)
            s.postorder(root.right)
            print(root.data,end=" --> ")

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
root.inorder(root)
print()
root.postorder(root)
print()
root.preorder(root)
