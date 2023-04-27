n=int(input())
m=int(input())
l=[i for i in range(n,m+1)]
ans=[]

# for i in range(len(l)):
#     for j in range(i,len(l)):
#         ans.append(l[i:j+1])

ans=[l[i:j+1] for i in range(len(l)) for j in range(i,len(l))]
print(ans)

c=0
for i in ans:
    if(sum(i)%2!=0):
        c+=1
print(c)