# P3.23

# gets user input for income amount for the year
income = float(input("Please enter your income for the year: $"))

# assigns tax value based on income range
if(income <= 50000):
   tax = 0.01
elif(50000 < income <= 75000):
   tax = 0.02
elif(75000 < income <= 100000):
   tax = 0.03
elif(100000 < income <= 250000):
   tax = 0.04
elif(250000 < income <= 500000):
   tax = 0.05
else:
   tax = 0.06

# type cast final income tax amount as string for print
finalIncome = str(round(income * tax, 2))

# final print statement
print("The income tax amount you owe is: $" + finalIncome)