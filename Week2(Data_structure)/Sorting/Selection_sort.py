# Selection Sort
def selection_sort(l):
    n=len(l)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if(l[min_index]>l[j]):
                min_index=j
        l[i],l[min_index]=l[min_index],l[i]
        print(l)

l=[5,7,3,2,10,8]
selection_sort(l)
for i in l:
    print(i,end=' ')
