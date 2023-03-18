#list
list1=[]
print(list1,type(list))
list2=[10,20.0,"kiran",2+3j]
print(list2)
list4=list([10,20,30])
print(list4)

print("/n--------------------------------------------------")
#append
list4.append(40)
print(list4)
#extends
list4.extend([50,60,70])
print(list4)

#insert

list4.insert(1,80)
print(list4)

#remove value
list4.remove(80)
print(list4)

#pop uses index
list4.pop(0)
print(list4)
list4.pop()
print(list4)#last value

#delete
del list4[1]

l=[1,5,3,7,5]
l.pop(3)
print(l)
