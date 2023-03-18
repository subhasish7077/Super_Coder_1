def find_pairs_of_numbers(l,n):
    val={}
    for i in l:
        if(i not in val.keys()):
            index=l.index(i)
            for j in l[index+1:]:
                if(i+j==n):
                    val[i]=j
                    l.remove(j)
    print(val)
    return len(val.keys())

l=[int(i) for i in input().split()]
n=int(input())
print(find_pairs_of_numbers(l,n))