def find_more_than_average(l):
    avg=sum(l)/len(l)
    count=0
    for i in l:
        if(i>avg):
            count+=1
    return count*10

def generate_frequency(l):
    f=[0]*26
    for i in l:
        f[i]+=1
    return f

def sort_marks(l):
    l.sort()
    return l

l=[int(i) for i in input().split()]
print("1. ",find_more_than_average(l))
print("2. ",generate_frequency(l))
print("3. ",sort_marks(l))