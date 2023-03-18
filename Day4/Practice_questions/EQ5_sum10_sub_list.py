# def sum_num(n):
#     s=0
#     for i in n:
#         s+=int(i)
#     return s
n=input()
p=[]
for i in range(len(n)):
    for j in range(i,len(n)):
        p.append(n[i:j+1])
print(p)
ans=[]
for i in p:
    if(sum([int(i) for i in list(i)])==10):
        ans.append(i)
print(ans)

