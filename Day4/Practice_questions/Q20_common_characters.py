s1=input()
s2=input()
ans=''
for i in s1:
    if i in s2 and i!=' ' and i not in ans:
        ans+=i
print(ans)