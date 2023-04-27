def Binary_search(l,key):
    p=0
    h=len(l)-1
    mid=(p+h)//2
    while(p<h):
        if(l[mid]==key):
            return mid+1
        elif(key>l[mid]):
            p=mid+1
            mid=(p+h)//2
        else:
            h=mid-1
            mid=(p+h)//2
    else:
        return 0
l=[int(i) for i in input().split()]
x=Binary_search(l,5)
if(x==0):
    print("Key Not Found")
else:
    print("The value {} found at index {}".format(5,x))