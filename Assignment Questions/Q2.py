'''
Write a python lambda expression for the following:
1. Find the modulo of two numbers and add it to the difference of the same two numbers.
2. Find the square root of a number using math library built-in function.
3. Find the square root of a number without using built-in function.
'''
# 1.
x=lambda a,b:(a%b)+(a-b)
print(x(6,5))

# 2.
import math
y=lambda x:math.sqrt(x)
print(y(4))
print(y(5))

# 3.
n=int(input())
z=lambda x : x**0.5
print(z(n))
    