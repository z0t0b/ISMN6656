# P2.32
# integer inputs
totalBookPrice = int(input("Please enter the total book price for the order: $"))
numberOfBooks = int(input("Please enter the number of books that are being ordered: "))

# value for upcoming while loop
value = 0

# dummy value for shippingCharge variable
shippingCharge = 0

# assign tax value for total book price
tax = 0.075 * totalBookPrice

# increments shipping charge by 2 for every book
while (value < numberOfBooks):
   shippingCharge += 2
   value += 1
   
# variable for price of the order
orderPrice = str(round(totalBookPrice + tax + shippingCharge, 2))

# print total price
print("\nThe price of the order is : $" + orderPrice)