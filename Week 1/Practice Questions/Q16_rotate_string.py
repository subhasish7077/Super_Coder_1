l=input().split(',')
for i in l:
    j=i.split(':')
    n=[int(k)*int(k) for k in j[1]]
    a=sum(n)
    if(a%2==0):
        j[0]=j[0][len(j[0])-1]+j[0][:len(j[0])-1]
    else:
        j[0]=j[0][2:]+j[0][:2]
    print(j[0])