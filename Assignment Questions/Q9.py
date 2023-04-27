'''
Write a python program that it should consist of special charnumbers and chars. if there 
are even numbers of special chars Then the series should start with even followed by odd
Input: 19@a42&516
Output: 492561
If there are odd numbers of special chars then the output will be starting with odd 
followed by even
Input: 5u6@25g7#@
Output: 56527
If there are any number of additional digits append them at last
'''
l=list(input())
count=0
el=[]
ol=[]
for i in l:
    if(i.isalnum()==False):
        count+=1
    elif(i.isdigit()):
        if(int(i)%2==0):
            el.append(i)
        else:
            ol.append(i)
ans=''
print(el)
print(ol)
if(count%2==0):
    i=len(el)
    while(i>0):
        ans+=el[len(el)-i]+ol[len(el)-i]
        i-=1
    else:
        ans+=''.join(ol[len(el):])
print(ans)
