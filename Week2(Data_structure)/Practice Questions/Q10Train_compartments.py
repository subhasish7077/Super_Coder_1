'''
A train is identified by its name and list of compartments.

The compartments are identified by its name,total seating capacity and 
the number of passengers.

Implement the class Train as given in the class diagram.
Train
- train_name
- compartment_list
__init__(train_name,compartment_list)
+ get_train_name()
+ get_compartment_list()
+ count_compartments ()
+ check_vacancy()

Write a python program to implement the following:
count_compartments()- returns the total number of compartments in the train
check_vacancy()-returns the count of the compartments in which more than 50% of 
                the seats are vacant
Note : Compartment list is maintained as a linked list where data in each node 
        refers to a compartment.

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

class compartments:
    def __init__(s,name,no_passengers,capacity):
        s.__name=name
        s.__capacity=capacity
        s.__no_passenger=no_passengers
    def get_capacity(s):
        return s.__capacity
    def get_no_passenger(s):
        return s.__no_passenger
    def get_name(s):
        return s.__name

class Train:
    def __init__(s,train_name,compantments) -> None:
        s.__tname=train_name
        s.__comoartment=compantments
    def get_train_name(s):
        return s.__tname
    def get_compartment_list(s):
        return s.__comoartment
    def count_compartments (s):
        x=s.__comoartment.head
        if(x is None):
            return 0
        c=0
        while(x):
            c+=1
            x=x.next
        return c

    def check_vacancy(s):
        x=s.__comoartment.head
        if(x is None):
            return 0
        c=0
        while(x):
            temp=(x.data.get_capacity()-x.data.get_no_passenger())/x.data.get_capacity()
            if(temp>0.5):
                c+=1
            x=x.next
        return c
    def display(s):
        x=s.__comoartment.head
        while(x):
            print(x.data.get_name(),end='-->')
            x=x.next
        print()
        

c1=compartments("SL",250,400)
c2=compartments("2AC",125,280)
c3=compartments("3AC",120,300)
c4=compartments("FC",160,300)
c5=compartments("1AC",100,210)
l=[c1,c2,c3,c4,c5]
c=linkedlist()
for i in l:
    c.add_at_end(i)
t=Train("rajya",c)
t.display()
print("capacity:",t.check_vacancy())
print("compntment:",t.count_compartments())

