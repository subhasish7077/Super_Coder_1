'''
Write a higher order function, sum_all() to calculate the sum of elements in a list.
sum_all() :- It accepts a list and calculates the sum of the elements in the list based 
             on the conditions being checked in the lambda expressions passed to it.
Only those values satisfying the condition should be included in the sum.
Write the following lambda expressions.
1. greater: To check whether a given number is greater than 10.
2. divide: To check whether a given number is divisible by 10 and not greater than 100.
3. range_of_values: To check whether a given number is between 25 and 50 (Both inclusive).
'''
def sum_all(l,greater=lambda x:x>10,divide=lambda x: x%10==0 and x%100!=0,range=lambda x: x in range(25,51)):
    l=[i for i in l if greater(i)==divide(i)==range(i)== True]
    return sum(l)
l=[1,2,3,4,5,6,7,8,9,10,30]
print(sum_all(l))