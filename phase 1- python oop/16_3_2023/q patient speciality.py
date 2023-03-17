d={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
l=list(map(str,input().split()))
def maxspeciality(l,d):
    c1=l.count("P")
    c2=l.count("O")
    c3=l.count("E")
    if c1>c2 and c1>c3:
        print(d["P"])
    elif c2>c1 and c2>c3:
        print(d["O"])
    else:
        print(d["E"])
maxspeciality(l,d)

#101 P 102 O 301 P 305 P
#101 O 102 O 302 P 305 E 401 O 656 O
