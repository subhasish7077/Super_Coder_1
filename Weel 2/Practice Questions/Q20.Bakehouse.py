'''
The owner of a BakeHouse wants to keep track of the tables that are occupied in his 
cafe. Assume that there are 10 tables in his cafe numbered from 1 to 10. As and when
a table is occupied, it must be added to the occupied_table_list and when a customer 
leaves, the corresponding table must be removed from the list.

BakeHouse
- occupied_table_list
_init_()
+ get_occupied_table_list()
+ allocate_table()
+ deallocate_table(table_number)

Write a python program to implement BakeHouse class. 
Represent occupied_table_list using an appropriate data structure.

Note: Table numbers should be maintained in ascending order 
      in the occupied_table_list.

Tables should be allocated and de-allocated as mentioned in the example below:
Example: Suppose tables 1, 2, 3 and 4 are initially allocated. 
         Now if a new customer arrives, he should be allocated table 5 and 
         the table list should be accordingly updated. If now customer at table 2 
         leaves, table list should be accordingly updated and the next new customer 
         should be allocated table 2 as it is the first free table.

Implement the allocation logic in allocate_table() method and de-allocation logic in
deallocate_table() method.
'''
class Table:
    def __init__(s,data) -> None:
        s.data=data
        s.next=None
class BakeHouse:
    __head=None
    def __init__(s):
        s.__head=None
    def get_occupied_table_list(s):
        temp=s.__head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next
        
    def allocate_table(s):
        p=2
        if(s.__head is None or s.__head.data!=1):
            n_table=Table(1)
            n_table.next=s.__head
            s.__head=n_table
            return
        else:
            temp=s.__head
            while(temp.next!=None):
                if(p==temp.next.data):
                    p+=1
                    temp=temp.next
                else:
                    break    
            n_table=Table(p)
            n_table.next=temp.next
            temp.next=n_table
    def deallocate_table(s,table_number):
        if(s.__head.data==table_number):
            s.__head=s.__head.next
        else:
            temp=s.__head
            while(temp.next!=None):
                if(temp.next.data==table_number):
                    break
                temp=temp.next
            temp.next=temp.next.next

bh=BakeHouse()
while(True):
    n=int(input('Enter 1 for allocate Table or 2 for deallocate table:'))
    if(n==1):
        bh.allocate_table()
        bh.get_occupied_table_list()
        print()
    elif(n==2):
        table_no=int(input('Enter Table no:'))
        bh.deallocate_table(table_no)
        bh.get_occupied_table_list()
        print()
    else:
        break

