#  Pattern
l=[]
n=int(input())
for i in range(0,n+2):
    l1=[]
    for j in range(0,n+2):
        if(i in [0,n+1] or j in [0,n+1]):
            l1.append("----")
        else:
            l1.append((i,j))
    l.append(l1)

l=[["----" if i in [0,n+1] or j in [0,n+1] else (i,j) for i in range(n+2)] for j in range(n+2)]
for i in l:
    print(i)