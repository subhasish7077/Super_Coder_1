def fun(a,b):
    print(type(a))
    print(type(b))
    return a+b

x=fun(10,20)
y=fun('sipu','lipu')
print(x)
print(y)

# 1.Positional arguments
print("\nPositional Arguments")
def fun(a,b,c,d):
    print("a=",a," b=",b," c=",c," d=",d)

fun(2,4,6,8)

# 2.Keyword Arguments
print("\nKeyword Arguments")
def fun(a,b,c,d):
    print("a=",a," b=",b," c=",c," d=",d)

fun(d=2,c=4,a=6,b=8)

# 3.Default Argument
print("\nDefault Arguments")
def fun(name,roll,branch,college="GIETU"):
    print("name=",name," roll=",roll," branch=",branch," college=",college)

fun("sipu",34,"CSE","BITs")
fun("lipu",38,"CSE")
fun("kiran",42,"Ag")

# 4.Variable no of Arguments
print("\nVariable no Arguments")
def fun(*var):
    sum=0
    for i in var:
        sum+=i
    print("sum=",sum)

fun(1,2,5,7,9,5)
fun(7,8,9)
fun(2,1,1)