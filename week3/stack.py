class stack:
    element=[None]
    present_size=0
    def __init__(s,max_size) -> None:
        s.__max_size=max_size
        t=[None]*max_size
        stack.element+=t
        s.__start=stack.present_size
        stack.present_size+=max_size
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
            stack.element[s.__start+s.__top]=val
            # print("sucessfully Inserted {} into the stack.".format(val))
    def top(s):
        return stack.element[s.__start+s.__top]
    def pop(s):
        if(s.isempty()):
            print("Cannot pop as the Stack is empty.")
        else:
            x=s.top()
            stack.element[s.__start+s.__top]=None
            s.__top-=1
            # print("sucessfully poped {} from the stack.".format(x))
            return x
    def get_max_size(s):
        return s.__max_size
    def increase_max_size(s,size):
        stack.element=stack.element[:s.__start+s.__max_size]+[None]*size+stack.element[s.__start+s.__max_size:]
        stack.present_size+=size
        s.__max_size=s.__max_size+size
    def display(s):
        if(s.isempty()):
            print("Stack is empty:")
        else:
            print("The Stack elements are: ",end="")
            for i in range(s.__top+1):
                print(stack.element[s.__start+i],end=' ')
            print()
    def display_all_stack():
        for i in range(stack.present_size):
            print(stack.element[i],end=' ')
        print()

s1=stack(5)
s2=stack(10)
s3=stack(5)

for i in range(1,6):
    s1.push(i)
for i in range(101,111):
    s2.push(i)
for i in range(21,26):
    s3.push(i)

s1.display()
s2.display()
s3.display()
print('total size:',stack.present_size)
print()
stack.display_all_stack()
print()
print('pop two element of s2')
s2.pop()
s2.pop()
s2.display()
stack.display_all_stack()
print('total size:',stack.present_size)
print()
print('new stack s4 and push 3 element')
s4=stack(3)
for i in range(666,669):
    s4.push(i)
s4.display()
stack.display_all_stack()
print('total size:',stack.present_size)

print()
print('increase size of s3 and pushed element + 5')
s3.increase_max_size(5)
s3.push(26)
s3.push(27)
s3.display()
stack.display_all_stack()
print('total size:',stack.present_size)