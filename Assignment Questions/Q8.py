'''
Special string reverse

special string reverse
Input Format: b@rd
output Format: d@rb
Explanation:
We should reverse the alphabets of the string by keeping the 
special characters in the same position.

'''
l=list(input())
i,j=0,len(l)-1
while(i<j):
    if(l[i].isalnum()==False or l[j].isalnum()==False):
        pass
    else:
        l[i],l[j]=l[j],l[i]
    i+=1
    j-=1
print(''.join(l))


'abcd@ui%cd'
'dcci@ud%ba'