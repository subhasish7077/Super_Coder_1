# Problem Statement:
# Write a python program to find and display the product of three positive 
# integer values based on the rule mentioned below:
# ·   It should display the product of the three values except when one of 
#     the integer value is 7.
# ·   In that case, 7 should not be included in the product and the values 
#     to its left also should not be included.
# ·   If there is only one value to be considered, display that value itself.
# ·   If no values can be included in theproduct, display -1.

# Note:Assume that if 7 is one of the positive integer values, 
#      then it will occur only once.

# Sample Input
# 1 5 3
# Sample Output
# 15

# Sample Input
# 4 7 8
# Sample Output
# 8


n=[int(i) for i in input().split()]
p=1
if(n[0]==7):
    print(n[1]*n[2])
elif(n[1]==7):
    print(n[2])
elif(n[2]==7):
    print(-1)
else:
    print(n[0]*n[1]*n[2])