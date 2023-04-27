s=input()
if(len(s)<2):
    print('-1')
else:
    ans=s[0:2]+s[-2:]
    print(ans)