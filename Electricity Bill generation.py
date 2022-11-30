#Electricity bill generation
#input : no of units consumed
#0-100=> 0.50 per unit
#100-150=>1.25 per unit
#150-200=>2.50 per unit


#a refers to unit consumed
a=int(input("Enter the unit consumed: "))

if a>=0 and a<100:
    print("Your bill is",a*0.50)

if a>=100 and a<150:
    print("Your bill is",a*1.25)

if a>=150:
    print("Your bill is",a*2.50)


