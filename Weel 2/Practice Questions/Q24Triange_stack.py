'''
Given a  queue of numbers. Write a python function to push every second elements in the 
queue to a stack, if it is the trianle number of the previous element in the queue and 
return the stack. The output stack should be of the same size as that of the input queue.

Number d is said to be a triange number of n, if 
d=1+2+3+...+(n-2)+(n-1)+n
for example 28 is said to be the triangle number of 7, 
as 1+2+3+4+5+6+7=28

Sample input                              
Input Queue (front -> rare): 7,28,8,35,3,6,5,15,2,5
Output stack (top --> bottom):15,6,28
'''

class Queue:
    def __init__(s,max_size):
        s.__max_size=max_size
        s.__element=[None]*max_size
        s.__front=0
        s.__rare=-1
    def isempty(s):
        if(s.__rare<s.__front):
            return True
        return False
    def isfull(s):
        if(s.__rare==s.__max_size-1):
            return True
        return False
    def equeue(s,data):
        if(s.isfull()):
            print('Queue is full')
        else:
            s.__rare+=1
            s.__element[s.__rare]=data
    def dqueue(s):
        if(s.isempty()):
            print('Queue is empty')
        else:
            x=s.__element[s.__front]
            s.__element[s.__front]=None
            s.__front+=1
            return x
    def display(s):
        for i in range(s.__front,s.__rare+1):
            print(i,end=' ')
        else:
            print()
    def get_max_size(s):
        return s.__max_size
    def peek(s):
        return s.__element[s.__front]
    def get_front(s):
        return s.__front
    def get_rare(s):
        return s.__rare

class stack:
    def __init__(s,max_size):
        s.max_size=max_size
        s.__top=-1
        s.__element=[None]*max_size
    def isfull(s):
        if(s.__top==s.max_size-1):
            return True
        return False
    def isempty(s):
        if(s.__top<0):
            return True
        return False
    def push(s,data):
        if(s.isfull()==False):
            s.__top+=1
            s.__element[s.__top]=data
        else:
            print('Stack is full')
    def pop(s):
        if s.isempty():
            print('Stack is empty')
        else:
            x=s.__element[s.__top]
            s.__top-=1
            return x
    def display(s):
        temp=s.__top
        while(temp>=0):
            print(s.__element[temp],end=' ')
            temp-=1
    def top(s):
        return s.__element[s.__top]

def triangle_stack(q):
    s=stack(q.get_max_size())
    while(q.isempty()==False):
        temp=q.dqueue()
        t_n=sum(range(temp+1))
        temp=q.dqueue()
        if(temp==t_n):
            s.push(temp)
    return s

l=[int(i) for i in input().split()]
max_size=len(l)
q=Queue(max_size)
for i in l:
    q.equeue(i)
s=triangle_stack(q)
s.display()