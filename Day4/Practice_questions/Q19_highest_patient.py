d={
    "P":"Pediatric",
    "O":"Orthopedics",
    "E":"ENT"
}

l=input().split()
d2={}
for i in range(1,len(l),2):
    if(l[i] not in d2.keys()):
        d2[l[i]]=1
    else:
        d2[l[i]]+=1
print(d2)
for i in d2.keys():
    if(d2[i]==max(d2.values())):
        print(d[i])