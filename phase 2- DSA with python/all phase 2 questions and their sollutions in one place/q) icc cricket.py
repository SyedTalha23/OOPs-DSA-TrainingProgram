"""The International Cricket Council (ICC) wanted to do some 
analysis of international cricket matches held in last 
10 years.

Given a list containing match details as shown below:
[match_detail1,match_detail2……]

Format of each match_detail in the list is as shown below:
country_name : championship_name : total_number_of_matches_played : number_of_matches_won
Example: AUS:CHAM:5:2 means Australia has participated in 
Champions Trophy 5 times and have won 2 times.

Write a python program which performs the following:

find_matches (country_name): Accepts the country_name and 
returns the list of details of matches played by that country.
max_wins(): Returns a dictionary containing the championship name as the key and the list of country/countries which have 
won the maximum number of matches in that championship as the value.
find_winner(country1,country2): Accepts name of two countries and returns the country name which has won more number 
of matches in all championships. If both have won equal number of matches, return "Tie".
Perform case sensitive string comparison wherever necessary.
match_list  ['ENG:WOR:2:0', 'AUS:CHAM:5:2', 'PAK:T20:5:1', 'AUS:WOR:2:1', 'SA:T20:5:0', 'IND:T20:5:3', 'PAK:WOR:2:0', 
'SA:WOR:2:0', 'SA:CHAM:5:1', 'IND:WOR:2:1']

Sample Input	    Expected Output
find_matches ("AUS")	['AUS:CHAM:5:2', 'AUS:WOR:2:1']
max_wins()	{'WOR': ['AUS', 'IND'], 'CHAM': ['AUS'], 'T20': ['IND']}
find_winner("AUS","IND")	IND
"""
class cricketAnalysis:
    def __init__(self,matchList):
        self.match_list=matchList
    
    def find_matches(self,country):
        l=[] 
        for i in self.match_list:
            if country in i:
                l.append(i)
        return l
    def max_wins(self):
        l=[]
        for i in self.match_list:
            l.append(i.split(":"))
        print(l) #[['ENG', 'WOR', '2', '0'], ['AUS', 'CHAM', '5', '2'], ['PAK', 'T20', '5', '1'], ['AUS', 'WOR', '2', '1'], ['SA', 'T20', '5', '0'], ['IND', 'T20', '5', '3'], ['PAK', 'WOR', '2', '0'], ['SA', 'WOR', '2', '0'], ['SA', 'CHAM', '5', '1'], ['IND', 'WOR', '2', '1']]
        cl=[]
        for i in l:
            if i[1] not in cl:
                cl.append(i[1])
        print(cl) #['WOR', 'CHAM', 'T20']
        mw=[]
        for i in cl:
            max=0
            for j in l:
                if j[1]==i:
                    if int(j[3])>max:
                        max=int(j[3])
            mw.append(max)
        print(mw)
        d={}
        for i in range(len(cl)):
                temp=[]
                for j in l:
                    if j[1]==cl[i] and int(j[3])==mw[i]:
                        temp.append(j[0])
                # d.update({cl[i]:temp})
                d[cl[i]]=temp
        print(d)

    def find_winner(self,country1,country2):
        c1wins=0
        c2wins=0
        for i in self.match_list:
            if country1 in i:
                c1wins=c1wins+int(i[-1])
            if country2 in i:
                c2wins=c2wins+int(i[-1])
        if c1wins>c2wins:
            return country1
        elif c2wins>c1wins:
            return country2
        else:
            return "TIE"


        
                
            

match_list = ['ENG:WOR:2:0', 'AUS:CHAM:5:2', 'PAK:T20:5:1', 'AUS:WOR:2:1', 'SA:T20:5:0', 'IND:T20:5:3', 'PAK:WOR:2:0', 
'SA:WOR:2:0', 'SA:CHAM:5:1', 'IND:WOR:2:1']
ca1=cricketAnalysis(match_list)
ca1.max_wins()
print(ca1.find_winner("AUS","IND"))

