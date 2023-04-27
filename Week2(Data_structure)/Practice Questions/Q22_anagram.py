def check_anagram(s1,s2):
    if(len(s1)!=len(s2)):
        return False
    for i in s1:
        if(s1.count(i)!=s2.count(i)):
            return False
    return True
s1=input().lower()
s2=input().lower()
print(check_anagram(s1,s2))
