taxrate=0.20
standardreduction=10000
dependantreduction=3000

grossincome=float (input("Enter your total income:"))
numberofdependant=int (input("Enter total number of dependant:"))

taxaebleincome=grossincome-standardreduction-dependantreduction*numberofdependant

incometax=taxaebleincome*taxrate

print("The income tax is $" + str(incometax))
