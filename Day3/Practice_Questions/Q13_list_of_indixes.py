# mylist=[int(i) for i in input().split()]
mylist=[9,3,6,1,5,0,8,2,4,7]

# list_b=[int(i) for i in input().split()]
list_b=[6,4,6,1,2,2,10]
ans=[(i,mylist.index(i)) if(i in mylist) else (i,"not in list") for i in list_b ]
print(ans) 


ans={i:mylist.index(i) if i in mylist else "not in my list" for i in list_b}
print(ans) 