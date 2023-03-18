def check_double(n):
    if(int(n)==0):
        print(False)
    else:
        x=list(str(int(n)*2))
        l1=list(n)
        x.sort()
        l1.sort() 
        if(x==l1):
            print(True)
        else:
            print(False)
        
    
n=input()
check_double(n)
