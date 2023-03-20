def count(s):
    lc=0
    nc=0
    for i in s:
        if(i.isalpha()):
            lc+=1
        if(i.isnumeric()):
            nc+=1
    return [lc,nc]

s=input()
print(count(s))