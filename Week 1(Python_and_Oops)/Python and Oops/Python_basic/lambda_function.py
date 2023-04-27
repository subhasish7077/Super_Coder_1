
# lambda function

x=lambda x:x*x
print(x(5)) #x returns square of a number

y=lambda a,b:a+b
print(y(5,6)) #y returns addition of two numbers

#lambda function can also be used as key factor to some inbuilt function

l=['abc','sipu','bcdf','kiran','lipu','aditi','bobble','selection']
# to sort the above list 'l' according to second character of the string
l.sort(key=lambda x:x[1])
print(l)

l=[[1,2],[4,6],[6,4],[3,5,6],[1,2,4,8]]
# sort the above list as per the second element of lists
l.sort(key=lambda x:x[1])
print(l)
