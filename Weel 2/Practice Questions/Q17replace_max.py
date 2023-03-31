'''
Given an linked list and replace the maximum value of the list with a given number.
'''
class Node:
    def __init__(s,data=None):
        s.data=data
        s.next=None
class linkedlist:
    def __init__(s) -> None:
        s.head=None
# Add nodes
    def add_at_end(s,data):
        n_node=Node(data)
        if(s.head==None):
            s.head=n_node
        else:
            temp=s.head
            while(temp.next != None):
                temp=temp.next
            temp.next=n_node
# Remove node
    def remove_frm_end(s):
        if(s.head is None):
            print("List is empty")
        else:
            n=s.head
            while(n.next.next is not None):
                n=n.next
            n.next=None
    def display(s):
        x=s.head
        while(x is not None):
            print(x.data,end=" ---> ")
            x=x.next
        print()
    def replace(s,val,r_val):
        temp=s.head
        while(temp):
            if(temp.data==val):
                temp.data=r_val
                break
            temp=temp.next
        else:
            print("Value not found")
    def max_value(s):
        temp=s.head
        m=-999999
        while(temp):
            m=max(temp.data,m)
            temp=temp.next
        return m
    
ll=linkedlist()
l=[int(i) for i in input().split()]
for i in l:
    ll.add_at_end(i)
replace_val=int(input())
ll.replace(ll.max_value(),replace_val)
ll.display()

