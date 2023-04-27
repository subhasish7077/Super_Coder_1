'''
Write a python lambda expression for calculating simple interest.
If simple interest is greater than 1000, display as “Platinum Member”, otherwise “Gold Member”.
Use the below formula to calculate the simple interest.
simple_interest=(principal_amount*duration in years*rate_of_interest)/100
'''
simple_interest=lambda p,t,r: (p*t*r)/100
p,t,r=map(int,input().split())
if(simple_interest(p,t,r)>1000):
    print("Platinum Member")
else:
    print("Gold Member")