'''
A non empty string instr containing only parenthesis (,),{.},[,] it return outstr based on following,
  instr is properly nested and return 0
  instr not properly nested, return position of element in instr
  position start from 1
Input: {([])} Output: 0
Input: (])()] Output: 3
Input: [[()]  Output: n+1 for last element i.e 5+1=6
'''
class stack:
    def __init__(s,max_size=100):
        s.__max_size=max_size
        s.__element=[None]*max_size
        s.__top=-1
    def isfull(s):
        if(s.__top==s.__max_size):
            return True
        return False
    def isempty(s):
        if(s.__top==-1):
            return True
        return False
    def push(s,data):
        if(s.isfull()==False):
            s.__top+=1
            s.__element[s.__top]=data
        else:
            print("Stack is full")
    def pop(s):
        if(s.isempty()==False):
            temp=s.__element[s.__top]
            s.__element[s.__top]=None
            s.__top-=1 
        else:
            print("Stack is empty")
    def top(s):
        return s.__element[s.__top]
    def display(s):
        for i in range(s.__top+1):
            print(s.__element[i],end=' ')
n=input()
s=stack()
count=0
for i in n:
    count+=1
    if i in ['(','[','{']:
        s.push(i)
    else:
        if(i==')' and s.top()=='('):
            s.pop()
        elif(i==']' and s.top()=='['):
            s.pop()
        elif(i=='}' and s.top()=='{'):
            s.pop()
        else:
            print(count)
            break
else:
    if(s.isempty()==False):
        print(count+1)
    else:
        print(0)
