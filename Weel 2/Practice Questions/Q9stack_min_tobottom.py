'''
Given a stack of integers, write a python program that updates the input stack such that
all occurance of the smallest value are at the bottom of the stack, while the order of 
the elements remains the same.

sample input:
5 66 5 7 8 

Output:
66 7 8 5 5
'''
class stack:
    def __init__(s,max_size) -> None:
        s.__max_size=max_size
        s.__element=[None]*s.__max_size
        s.__top=-1
    def isempty(s):
        if(s.__top==-1):
            return True
        else:
            return False
    def isfull(s):
        if(s.__top==s.__max_size-1):
            return True
        else:
            return False
    def push(s,val):
        if(s.isfull()):
            print("Cannot push as stack is full.")
        else:
            s.__top+=1
            s.__element.insert(s.__top,val)
            # print("sucessfully Inserted {} into the stack.".format(val))

    def top(s):
        return s.__element[s.__top]
    def pop(s):
        if(s.isempty()):
            print("Cannot pop as the Stack is empty.")
        else:
            x=s.top()
            s.__top-=1
            s.__element.pop()
            # print("sucessfully poped {} from the stack.".format(x))
            return x
    def get_max_size(s):
        return s.__max_size
    def display(s):
        if(s.isempty()):
            print("Stack is empty:")
        else:
            print("The Stack elements are: ",end="")
            for i in range(s.__top+1):
                print(s.__element[i],end=' ')
            print()

def function(s):
    m=999999
    freq=1
    temp=stack(s.get_max_size())
    while(s.isempty()==False):
        t=s.pop()
        if(m!=min(m,t)):
            m=min(m,t)
            freq=1
        elif(m==t):
            freq+=1
        temp.push(t)
    # # print(m)
    # print(freq)
    while(temp.isempty()==False):
        t=temp.pop()
        if(t!=m):
            s.push(t)
    for i in range(freq):
        s.push(m)
    s.display()

s=stack(5)
l=[int(i) for i in input().split()]
for i in l:
    s.push(i)
# s.display()
# print(s.top())
function(s)
'''
s=5 66 8 7 5
temp=

s=5 66 8 7
temp=5

s=5 66 8
temp=5 7

s=5 66
temp=5 7 8

s=5
temp=5 7 8 66

s=66 8 7 
temp=5 5
'''
