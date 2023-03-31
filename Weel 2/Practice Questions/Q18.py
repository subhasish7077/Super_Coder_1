class people:
    def __init__(s,name,age,gender):
        s.name=name
        s.age=age
        s.gender=gender
    def get_name(s):
        return s.name
    def get_age(s):
        return s.age
    def get_gender(s):
        return s.gender
class queus:
    def __init__(s,max_size) -> None:
        s.__max_size=max_size
        s.__element=[None]*max_size
        s.__front=0
        s.__rare=-1
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
            # print("inserted {} in the Queue".format(s.__element[s.__rare]))
    def dqueue(s):
        if(s.isempty()):
            print("Queue is empty")
        else:
            x=s.__element[s.__front]
            s.__element[s.__front]=None
            s.__front+=1
            return x
    def get_max_size(s):
        return s.__max_size
    def display(s):
        print("The Queue elements are: ",end="")
        for i in range(s.__front,s.__rare+1):
            print(s.__element[i],end=" ")
        print()
    def get_present_size(s):
        return s.__rare-s.__front+1
def get_female(q):
    temp=queus(q.get_present_size())
    for i in range(q.get_present_size()):
        x=q.dqueue()
        if(x.get_gender()=='Female'):
            print(x.get_name()," ",x.get_age()," ",x.get_gender())

    
p1=people('Sipu',23,'Male')
p2=people('Lipu',23,'Male')
p3=people('Aditi',23,'Female')
p4=people('Kiran',23,'Male')
p5=people('Chandan',23,'Female')
pq=queus(5)
l=[p1,p2,p3,p4,p5]
for i in l:
    pq.enqueue(i)
get_female(pq)
