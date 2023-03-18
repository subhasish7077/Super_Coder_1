def translate(l,d):
    ans=[]
    for i in l:
        ans.append(d[i])
    return ans

d={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
n=input().split()
print(translate(n,d))