def numofcoin(rs5coin,rs1coin,amount):
    if (rs5coin*5+rs1coin*1)<amount:
        print(-1)
    else:
        temp1=amount//5
        temp2=amount-(temp1*5)
        print("number of 5 rs coin required= ",temp1)
        print("number of 1 rs coin required= ",temp2)
numofcoin(4,2,21)
numofcoin(2,11,11)
numofcoin(3,3,19)
        
        
