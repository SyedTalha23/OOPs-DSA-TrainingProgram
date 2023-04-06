'''
Write a python program to help an airport manager to generate
 few statistics based on the ticket details available for a 
day.
Go through the below program and complete it based on the comments mentioned in it.
Note: Perform case sensitive string comparisons wherever necessary.

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", 
"BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015",
"AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
#find_passengers_per_flight()
print(sort_passenger_list())
'''
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", 
"BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015",
"AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(airline_name):
    l=[]
    for i in ticket_list:
        if i[:2]==airline_name:
            l.append(i)
    return l
def find_passengers_destination(destination):
    l=[]
    for i in ticket_list:
        if i[10:13]==destination:
            l.append(i)
    return l
def find_passengers_per_flight():
    fl=[]
    for i in ticket_list:
        if i[:5] not in fl:
            fl.append(i[:5])
    print(fl)
    
    ppf={}
    for i in fl:
        counter=0
        for j in ticket_list:
            if i==j[:5]:
                counter+=1
        ppf[i]=counter
    print(ppf)

def sort_passenger_list():
    ticket_list.sort()
    return ticket_list


print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
find_passengers_per_flight()
print(sort_passenger_list())