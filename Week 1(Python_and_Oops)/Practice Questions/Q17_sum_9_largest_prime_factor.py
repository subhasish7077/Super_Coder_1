def is_prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False 
    return True
def largest_prime_factor(n):
    m=0
    for i in range(1,n+1):
        if(is_prime(i)):
            if(n%i==0):
                # print(i)
                m=max(m,i)
    return m
n=int(input())
s=0
for i in range(n,n+9):
    x=largest_prime_factor(i)
    print(x,end=' ')
    s+=x
print(s)
