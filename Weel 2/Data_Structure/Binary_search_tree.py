'''
Binary Search Tree is a node-based binary tree data structure which has the 
following properties.

The left subtree of a node contains only nodes with keys lesser than the node's key.

The right subtree of a node contains only nodes 

'''
class Node:
    def __init__(s,data=None,left=None,right=None):
        s.data=data
        s.left=left
        s.right=right
    def inorder(s,root):
        if(root):
            s.inorder(root.left)
            print(root.data,end=" --> ")
            s.inorder(root.right)
def insert(root,key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    return root
def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def delete(root,key):
    if root is None:
        return None
    if key<root.data:
        root.left=delete(root.left,key)
    elif key>root.data:
        root.right=delete(root.right,key)
    else:
        if root.right is None:
            temp=root.left
            root=None
            return temp
        if root.left is None:
            temp=root.right
            root=None
            return temp
        temp=minValueNode(root)
        root.data=temp.data
        root.right=delete(root.right,temp.data)
    return root 



root=None
root=insert(root,8)
root=insert(root,3)
root=insert(root,1)
root=insert(root,6)
root=insert(root,7)
root=insert(root,10)
root=insert(root,14)
root=insert(root,4)
root=insert(root,2)
root=insert(root,9)

root.inorder(root)
root=delete(root,1)
print()
