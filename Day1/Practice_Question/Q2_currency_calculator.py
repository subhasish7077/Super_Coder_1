def currencyConvertor(amountINR,country):
    if(country=="Euro"):
        return amountINR*0.01417
    elif(country=="British Pound"):
        return amountINR*0.0100
    elif(country=="Australian Dollar"):
        return amountINR*0.02140
    elif(country=="Canadian Dollar"):
        return amountINR*0.02027
    else:
        return -1

print("Select currency as per the list and the amount in INR:")
cur_list = {1:"Euro",2:"British Pound",3:"Australian Dollar",4:"Canadian Dollar",5:"Invalid"}
for i in cur_list.keys():
    print(i,"->",cur_list[i])

cur=int(input())
amt=int(input())

print(currencyConvertor(amt,cur_list[cur]))

