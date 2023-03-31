''' 
Given two integers n and k. Find the position of the nth multiple of K in the 
    Fibonacci series. 
#Examples:

#Input: k = 2, n = 3
#Output: 9, 3rd multiple of 2 in Fibonacci Series is 34 that appears at position 9.

#Input: k = 4, n = 5 
#Output: 30, 5th multiple of 4 in Fibonacci Series is 832040 which appears at position 30
'''
n=[int(i) for i in input().split()]
a,b,c=0,1,1
while(n[1]>0):
    if((a+b)%n[0]==0):
        n[1]-=1
    a,b=b,a+b
    c+=1
print(c)

