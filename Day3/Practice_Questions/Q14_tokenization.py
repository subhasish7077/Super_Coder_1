sentence=["a new world record was set",
          "in the holy city of ayodhya",
          "on the eve of diwali on tuesday",
          "with over three lakhs diya or earthen lamps",
          "lit up simontanously on the bank of the sarayu river"]
stopwords=["for","a","of","the","and","to","in","on","with","was","or"]

ans=[j for i in sentence for j in i.split() if(j not in stopwords)]

for i in ans:
    print(i)
