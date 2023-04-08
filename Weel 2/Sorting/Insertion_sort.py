def insertion_sort(l):
    i=0
    while(i<len(l)):
        j=i
        while(j>0 and l[j]<l[j-1]):
            l[j],l[j-1]=l[j-1],l[j]
            j-=1
        i+=1

l=[1,4,2,6,3,8,10,40,59,43,68,59,93]
insertion_sort(l)
print(l)
