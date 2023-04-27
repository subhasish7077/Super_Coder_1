'''
Mary is a kindergarten teacher. She has given a task to the children after teaching them a list of words. 
The task is to find the unknown words (other than the words they already know) from the given text. 
Write a python function which accepts the text and the known list of words and returns the set of unknown words
found.
Return -1 if there are no unknown words.
Estimated Time: 20 minutes
Sample Input
Text: "the sun rises in the east"
Vocabulary:["sun","in,"east","doctor","day"]
Expected Output
{'rises','the'}
'''
def check(text,vocabulary):
    ans=set()
    for i in text:
        if i not in Vocabulary:
            ans.add(i)
    if(len(ans)):
        return ans
    return -1
    
text=input().split()
Vocabulary=input().split()
print(check(text,Vocabulary))