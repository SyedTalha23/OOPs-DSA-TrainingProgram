def cost(adults,childrens):
    temp=(37550.0*adults + (37550.0*childrens)/3)
    temp2=temp+temp*(7/100)
    cost=temp2-temp2*(10/100)
    print("total ticket cost:",cost)
cost(5,2)
cost(3,1)
