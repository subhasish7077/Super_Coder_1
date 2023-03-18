# Longest Substring

w1,w2=input().split()
ans=[[0 for i in range(len(w2)+1)] for j in range(len(w1)+1)]
val=-1
r=0
c=0
for i in range(len(w1)+1):
    for j in range(len(w2)+1):
        if(i==0 or j==0):
            ans[i][j]=0
        elif(w1[i-1]==w2[j-1]):
            ans[i][j]=ans[i-1][j-1]+1
            if(ans[i][j]>=val):
                val=max(ans[i][j],val)
                r=i
                c=j
        else:
            ans[i][j]=0
# for i in ans:
#     print(i)
# print(val)
a=''
while(ans[r][c]>0):
    a=w1[r-1]+a
    r-=1
    c-=1
print(a)