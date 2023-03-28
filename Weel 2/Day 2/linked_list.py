class Node:
    def __init__(s,data=None):
        s.data=data
        s.next=None
class linkedlist:
    def __init__(s) -> None:
        s.head=None
# Add nodes
    def add_at_beginning(s,data): 
        n_node=Node(data)
        n_node.next=s.head
        s.head=n_node
    def add_at_end(s,data):
        n_node=Node(data)
        if(s.head==None):
            s.head=n_node
        else:
            temp=s.head
            while(temp.next != None):
                temp=temp.next
            temp.next=n_node
    def add_after_loc(s,data,prev):
        temp=s.head
        for i in range(prev-1):
            temp=temp.next
        n_node=Node(data)
        n_node.next=temp.next
        temp.next=n_node 
# Remove node
    def remove_frm_beginning(s):
        if(s.head is None):
            print("List is empty")
        else:
            s.head=s.head.next
    def remove_frm_end(s):
        if(s.head is None):
            print("List is empty")
        else:
            n=s.head
            while(n.next.next is not None):
                n=n.next
            n.next=None
    def remove_by_loc(s,loc):
        if(s.head==None):
            print("List is empty")
        else:
            temp=s.head
            for i in range(loc-2):
                temp=temp.next
            temp.next=temp.next.next

    def display(s):
        x=s.head
        while(x is not None):
            print(x.data,end=" ---> ")
            x=x.next
        print()
    def no_of_node(s):
        if(s.head == None):
            return 0
        n=s.head
        c=0
        while(n):
            n=n.next
            c+=1
        return c
l=[int(i) for i in input().split()]
ll=linkedlist()
for i in l:
    ll.add_at_beginning(i)
ll.display()
print()
ll.remove_by_loc(3)
ll.display()
ll.remove_frm_beginning
ll.display()
print("Number of nodes: ",ll.no_of_node())