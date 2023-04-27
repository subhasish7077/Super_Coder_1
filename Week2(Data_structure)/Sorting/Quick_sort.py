# Quick Sort
def partision(ar,l,h):
    i=l-1
    pivot=ar[h]
    for j in range(l,h):
        if(ar[j]<pivot):
            i+=1
            ar[i],ar[j]=ar[j],ar[i]
    ar[i+1],ar[h]=ar[h],ar[i+1]
    return i+1
def quick_sort(ar,l,h):
    if(l<h):
        p=partision(ar,l,h)
        quick_sort(ar,l,p-1)
        quick_sort(ar,p+1,h)

l=[9,5,2,8,6,1,10,7]
quick_sort(l,0,len(l)-1)
print(l)
