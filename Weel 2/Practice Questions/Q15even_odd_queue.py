'''
Sample Input:                   Expexted Output:
2 7 9 4 6 5 10                  Odd queue: 7 9 5
                                Even Queue: 2 4 6 10
'''
class queue:
    def __init__(s,max_size):
        s.__max_size=max_size
        s.__element=[None]*max_size
        s.__rare=-1
        s.__front=0
    def isfull(s):
        if(s.__rare==s.__max_size-1):
            return True
        return False
    def isempty(s):
        if(s.__front>s.__rare):
            return True
        return False
    def enqueue(s,val):
        if(s.isfull()):
            print("Queue is full")
        else:
            s.__rare+=1
            s.__element[s.__rare]=val
    def dqueue(s):
        if(s.isempty()):
            print("Queue is empty")
        else:
            x=s.__element[s.__front]
            s.__element[s.__front]=None
            s.__front+=1
            return x
    def display(s):
        print("The Queue elements are: ",end="")
        for i in range(s.__front,s.__rare+1):
            print(s.__element[i],end=" ")
        print()
    def get_maxsize(s):
        return s.__max_size
    def get_front(s):
        return s.__front
    def get_rare(s):
        return s.__rare
    def get_present_size(s):
        return s.__rare-s.__front+1
    
def even_odd(q):
    eq=queue(q.get_maxsize())
    oq=queue(q.get_maxsize())
    for i in range(q.get_present_size()):
        x=q.dqueue()
        if(x%2==0):
            eq.enqueue(x)
        else:
            oq.enqueue(x)
    eq.display()
    oq.display()
q=queue(10)
l=[int(i) for i in input().split()]
for i in l:
    q.enqueue(i)
# print(q.get_present_size())
even_odd(q)
# q.display()




