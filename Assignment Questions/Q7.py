'''
An array is given suppose a =[3,5,8,2,19,12,7,11] One have to find the largest subarray 
that the element satisfy the following condition:
    x[i]=x[i-1]+x[i-2]

[2,3,5,8],[3,8,11],[2,5,7,12,19]
'''
l=[int(i) for i in input().split(',')]
l.sort(reverse=True)
print(l)
d={}
for i in l:
    d[i]=[]
    for j in range(len(l)):
        if(i-l[j] in l):
            t=sorted([l[j],i-l[j]])
            if(t not in d[i]):
                d[i].append(t)
ans=[]
print(d)
for i in l:
    for j in d[i]:
        temp=[i]
        temp.append(j[1])
        temp.append(j[0])
        k=temp[1]
        while(len(d[k])==0 or d[k][0][0]<temp[len(temp)-1]):
            temp.append(d[k][0][1])
            temp.append(d[k][0][0])
    # print(temp)