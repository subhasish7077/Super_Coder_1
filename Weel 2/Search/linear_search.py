def linear_search(l:list,key:int)->int :
    for i in range(len(l)):
        if(l[i]==key):
            return i+1
    return "Key not found"

l=[int(i) for i in input().split()]
key=int(input())
print("The index of {} is {}".format(key,linear_search(l,key)))