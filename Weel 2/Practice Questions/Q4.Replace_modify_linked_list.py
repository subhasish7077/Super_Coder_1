'''
Given a linked list of characters. write a python function that returns a new string 
that is created by appending all the characters given in the linked list as per the rules 
given below.

Rules:
Replace '*' or '/' by a single space.

In case of two consecutive occurrence of * or /, replace those two by a single space 
and convert the next character to upper case.

Assume that there will not be more than two consecutive occurrences of '*' or'/'.
The Linked list will always end with an alphabet.

Sample Input:
A,n,*,/,a,p,p,l,e,*,a,/,day,*,*,k,e,e,p,s,/,*,a,/,/,d,o,c,t,o,r,*,A,w,a,y

Output:
An Apple a day Keeps A Doctor Away

'''
class Node:
    def __init__(s,data=None):
        s.data=data
        s.next=None
class linkedlist:
    def __init__(s) -> None:
        s.head=None
#Add nodes
    def add_at_end(s,data):
        n_node=Node(data)
        if(s.head==None):
            s.head=n_node
        else:
            temp=s.head
            while(temp.next != None):
                temp=temp.next
            temp.next=n_node

    def display(s):
        x=s.head
        ans=""
        while(x is not None):
            # print(x.data,end=" ---> ")
            ans=ans+x.data
            x=x.next
        print(ans)

def replace(l):
    n=l.head
    while(n.next is not None):
        if(n.data=='*' or n.data=='/') and (n.next.data=='*' or n.next.data=='/'):
            n.data=' '
            n.next=n.next.next
            n.next.data=n.next.data.upper()
        elif(n.data=='*' or n.data=='/'):
            n.data=' '
        n=n.next


l=[i for i in input().split(',')]
ll=linkedlist()
for i in l:
    ll.add_at_end(i)
# ll.display()
replace(ll)
ll.display()