'''
Write a python program that accepts a text and displays a string which contains the 
word with the largest frequency in the text and the frequency itself separated by a 
space.
Rules:
The word should have the largest frequency. In case multiple words have the same 
frequency, then choose the word that has the maximum length.
Assumptions:
The text has no special characters other than space.
The text would begin with a word and there will be only a single space between the words.
Perform case insensitive string comparisons wherever necessary.
'''
text=[i.lower() for i in input().split()]
d={i:text.count(i) for i in text }
m=max(list(d.values()))
ans=''
for i in d:
    if(d[i]==m):
        ans=max([ans,i],key=len)
print(ans," ",m)

