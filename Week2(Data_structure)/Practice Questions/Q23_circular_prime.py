'''
The number, 197, is called a circular prime because all
rotations of the digits: 197, 971, and 719, are themselves
prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 
13, 17, 31, 37, 71, 73, 79, and 97.

Write a python program to find and display the number of 
circular primes less than the given limit.
'''

def rotate(s):
    return s[len(s)-1]+s[:len(s)-1]
n=int(input())
ans=[]
for i in range(2,n+1):
    temp=i
    for j in range(len(str(i))):
        if(abs(2**temp%temp-1) !=1):
            break
        temp=int(rotate(str(i)))
    else:
        ans.append(i)
print(ans)