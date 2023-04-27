'''
The International Cricket Council (ICC) wanted to do some analysis of 
international cricket matches held in last 10 years.

Given a list containing match details as shown below:
[match_detail1,match_detail2……]

Format of each match_detail in the list is as shown below:
country_name : championship_name : total_number_of_matches_played : number_of_matches_won
Example: AUS:CHAM:5:2 means Australia has participated in Champions Trophy 5 times 
         and have won 2 times.

Write a python program which performs the following:

find_matches(country_name): Accepts the country_name and returns the list 
            of details of matches played by that country.
max_wins(): Returns a dictionary containing the championship name as the key and 
            the list of country/countries which have won the maximum number of matches 
            in that championship as the value.
find_winner(country1,country2): Accepts name of two countries and returns the country 
            name which has won more number of matches in all championships. If both 
            have won equal number of matches, return "Tie".
Perform case sensitive string comparison wherever necessary.
match_list:['ENG:WOR:2:0', 'AUS:CHAM:5:2', 'PAK:T20:5:1', 'AUS:WOR:2:1', 'SA:T20:5:0',
              'IND:T20:5:3', 'PAK:WOR:2:0', 'SA:WOR:2:0', 'SA:CHAM:5:1', 'IND:WOR:2:1']

Sample Input	                Expected Output
find_matches ("AUS")	        ['AUS:CHAM:5:2', 'AUS:WOR:2:1']
max_wins()	                    {'WOR': ['AUS', 'IND'], 'CHAM': ['AUS'], 'T20': ['IND']}
find_winner("AUS","IND")	    IND
'''
# Using Linked List
class details:
    data=None
    next=None
    def __init__(s,data,next=None):
        s.data=data
        s.next=next
# Data is a string that contains the match detail
# country_name:championship_name:total_number_of_matches_played:number_of_matches_won
class match:
    match_detail=None
    def __init__(s):
        s.match_detail=None
    def add_match_detail(s,data):
        n_details=details(data)
        if(s.match_detail==None):
            s.match_detail=n_details
        else:
            temp=s.match_detail
            while(temp.next):
                temp=temp.next
            temp.next=n_details
    def find_matches(s,country_name):
        temp=s.match_detail
        match_list=[]
        while(temp):
            match_data=temp.data.split(':')
            if(match_data[0]==country_name):
                match_list.append(temp.data)
            temp=temp.next
        return match_list
    def max_wins(s):
        d={}
        temp=s.match_detail
        while(temp):
            match_data=temp.data.split(':')
            if(match_data[1] not in d):
                d[match_data[1]]=[[match_data[0],match_data[3]]]
            else:
                d[match_data[1]].append([match_data[0],match_data[3]])
            temp=temp.next
        for i in d.keys():
            m=max(d[i],key=lambda x:x[1])
            l=[]
            for j in d[i]:
                if(m[1]==j[1]):
                    l.append(j[0])
            d[i]=l
        return d
    def find_winner(s,country1,country2):
        temp=s.match_detail
        c1_count=0
        c2_count=0
        while(temp):
            match_data=temp.data.split(':')
            if(match_data[0]==country1):
                c1_count+=int(match_data[3])
            elif(match_data[0]==country2):
                c2_count+=int(match_data[3])
            temp=temp.next
        if(c1_count>c2_count):
            return country1
        elif(c2_count>c1_count):
            return country2
        else:
            return 'Tie'
        

match_list=['ENG:WOR:2:0', 'AUS:CHAM:5:2', 'PAK:T20:5:1', 'AUS:WOR:2:1', 'SA:T20:5:0',
              'IND:T20:5:3', 'PAK:WOR:2:0', 'SA:WOR:2:0', 'SA:CHAM:5:1', 'IND:WOR:2:1']
m=match()
for i in match_list:
    m.add_match_detail(i)
print(m.find_matches('AUS'))
print(m.max_wins())
print(m.find_winner('AUS','IND'))