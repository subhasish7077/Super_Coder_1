'''
For a given list of numbers find the its factors and add the factors then if the sum of all factor is 
present in original list, sort it and print it
Ex:
Input: 0,1,6
Factors: 0 = 0, sum =0
1 = 1, sum =1
6 =1,2,3 = sum =6
Output: 1,6
If the sum is not present in the list then return -1
'''
def factors(n):
    ans=[]
    for i in range(1,n//2+2):
        if n%i==0:
            ans.append(i)
    return sum(ans)
l=[int(i) for i in input().split() if int(i)>0]
for i in l:
    if(factors(i) not in l):
        print(-1)
        break
else:
    l.sort()
    print(l)