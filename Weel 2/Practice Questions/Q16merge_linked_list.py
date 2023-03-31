class Node:
    def __init__(s,data):
        s.data=data
        s.next=None
class LinkedList:
    def __init__(s) -> None:
        s.head=None
    def add_at_end(s,data):
        n_node=Node(data)
        if(s.head is None):
            s.head=n_node
        else:
            temp=s.head
            while(temp.next):
                temp=temp.next
            temp.next=n_node
    def display(s):
        if(s.head is None):
            return "List is empty"
        temp=s.head
        while(temp):
            print(temp.data,end='-->')
            temp=temp.next
        print()
def mearge(ll1,ll2,n):
    temp1=ll1.head
    temp2=ll2.head
    newll=LinkedList()
    for i in range(n):
        newll.add_at_end(temp1.data)
        temp1=temp1.next
    while(temp2):
        newll.add_at_end(temp2.data)
        temp2=temp2.next
    while(temp1):
        newll.add_at_end(temp1.data)
        temp1=temp1.next
    newll.display()
    

ll1=LinkedList()
ll2=LinkedList()
l1=[int(i) for i in input().split()]
l2=[int(i) for i in input().split()]
n=int(input())
for i in l1:
    ll1.add_at_end(i)
for i in l2: 
    ll2.add_at_end(i)
ll1.display()
ll2.display()
mearge(ll1,ll2,n)
