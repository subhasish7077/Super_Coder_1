# Alphabet with corresponding numbers
sen=input()
sen=sen.lower()
ans=[ord(i)-ord('a')+1 if i!=' ' else i for i in sen]
print(ans)