print("Hey there! welcome to the first SROI calculator built in Python. Did you know SROI is a big friggin' deal? We're going to create that calculation now.")
Deadweight = float(input("Deadweight is the counterfactual, usually a benchmark value. How much is your deadweight?\n Expects decimal (Ex: 0.5) > "))
Attribution = float(input("Attribution helps establish additional counterfactual, usually collected from beneficiaries. How much is your attribution?\n Expects decimal (Ex: 0.5) > "))
Displacement = float(input("Displacement helps establish whether or not you've displaced other activities achieving the same outcomes. It can be calculated from a variety of sources. How much is your displacement?\n Expects decimal (Ex: 5) > "))
Dropoff = float(input("Dropoff is looks out how much the outcome 'dropoffs' over each year the outcome is experienced. How much is your dropoff?\n Expects decimal (Ex: 0.5) > "))
FP = float(input("Financial proxies help you value the outcome. It's a monetary value. What's the value of your financial proxy?\n (Ex: 500) >"))
Q = float(input("Quantity refers to how many people you observed the change with. It's a frequency value. What is your quantity?\n (Ex: 12) >"))
Impact=(FP*Q)*((1-Deadweight)*(1-Attribution)*(1-Displacement))
print("Here's your impact, taking into consideration the deadweight, attribution, and displacement adjustments:")
print(Impact)
YearOne=Impact*(1-Dropoff)
YearTwo=YearOne*(1-Dropoff)
YearThree=YearTwo*(1-Dropoff)
YearFour=YearThree*(1-Dropoff)
YearFive=YearFour*(1-Dropoff)
TB1=int(YearOne)
TB2=int(YearOne+YearTwo)
TB3=int(YearOne+YearTwo+YearThree)
TB4=int(YearOne+YearTwo+YearThree+YearFour)
TB5=int(YearOne+YearTwo+YearThree+YearFour+YearFive)
Duration = int(input("How many years do these outcomes exist for?\n"))
print("Great! Thanks for that info. That means your total benefit is:")
if(Duration==1):
	print(TB1)
elif(Duration==2):
	print(TB2)
elif(Duration==3):
	print(TB3)
elif(Duration==4):
	print(TB4)
elif(Duration==5):
	print(TB5)
elif(Duration>5):
	print("You broke the system! We can only calculate up to five years :(")
